# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does
1. A writer sends their text and creator_id to POST /submit.
2. The service checks that the input is valid and assigns a unique content_id.
3. The model signal reads the text and produces a score indicating how AI-like it appears.
4. The style signal measures sentence length variation, word variety, and punctuation patterns.
5. The combining rule combines both signal scores into one overall score.
6. The score maps to a full-sentence label: high-confidence human, unsure, or high-confidence AI.
7. The service records the decision in the audit log and returns the content_id, guess, confidence, label, and both signal scores.


### When the system wrongly flags human writing

A writer submits a piece they wrote themselves. In this hypothetical
example, the combined AI-likelihood score is 0.92 and falls in the
high-confidence AI range.

The label says: "Our automated checks suggest this text may be
AI-generated. This result can be wrong. If you wrote it yourself,
you can request a review."

The writer sends the content_id and their explanation to POST /appeal.
The service records the appeal, changes the item's status to
under_review, and confirms that the appeal was received.
The original decision remains in the audit log.
An appeal does not automatically rerun the detector or reverse the decision.

---

## Signals and Scoring

The signals disagreed on both human-written samples. For my
formal email, the model returned 0.6694 while the style signal
returned 0.2999. Equal weighting produced 0.48465, near the
middle. This shows that predictable human writing can receive
a high model score.

The edited AI sample scored 0.6672, compared with 0.6608 for
the original. These edits did not reduce the combined score.

### Signal one — the model signal

**What it measures:** A local detector model scores how closely the writing resembles patterns it learned from human and AI-generated text.

**Why that might differ between human and AI writing:** Human and AI-generated writing may show different patterns in wording and sentence structure that the model learned during training.

**What it can't see:** It cannot verify who actually wrote the text or how it was created. Formal human writing may look AI-generated, and edited AI text may look human.

### Signal two — the style signal

**What it measures:** Sentence length variation, the ratio of unique words to total words, and punctuation density.

**Why that might differ between human and AI writing:** Some AI-generated writing may be more uniform or repetitive, while human writing may vary more. These are clues, not reliable rules.

**What it can't see:** It does not understand meaning or verify authorship. A human can write in a regular style, and AI text can be edited to change these statistics.

### The combining rule

**The rule:**

I use an equal-weight average of the model and style signals.
Both scores run from 0 to 1, with higher values meaning more
AI-like text. When they disagree, the average falls between them.
These scores are experimental indicators, not verified probabilities.

**The numbers:**

combined_score = 0.5 * model_score + 0.5 * style_score

The weights are stored in config.py:
- WEIGHT_MODEL_SIGNAL = 0.5
- WEIGHT_STYLE_SIGNAL = 0.5

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**

For the sample beginning "The system works well.", the model
returned 0.6722 and the style signal returned 0.4769.
Their equal-weight average is 0.57455, between the two scores.

For my short human-written sentence, the model returned 0.028
and the style signal returned its short-text fallback of 0.5.
The combined score would be 0.264. The fallback pulls the score
toward the middle; it does not provide evidence of AI authorship.


---
## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0 ≤ score ≤ 0.35 | Our automated checks suggest this text was written by a person. This result is not proof of authorship. |
| unsure | 0.35 < score < 0.65 | Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review. |
| high-confidence AI | 0.65 ≤ score ≤ 1 | Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review. |

**Why I worded the "unsure" one this way:**

The label explains that the system cannot confidently decide,
without accusing the writer. It also tells the writer that
they can request a review.

Actual submissions produced all three labels:
- Human sentence: 0.264, human.
- Formal human email: 0.48465, unsure.
- AI-generated paragraph: 0.6608, ai.
---
## Sample Run

**A submission**

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"Dear Team manager, I hope this email finds you well. I would like to let you know that due to unforeseen reasons I will not be able to submit my work progress and do presentations. I will resume my work and presentation next week. Thank you !","creator_id":"calibration-formal-human"}'
```

```json
{
  "confidence": 0.48465,
  "content_id": "83627415-6d70-4e9f-a74c-190408966f51",
  "guess": "unsure",
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "model_score": 0.6694,
  "status": "scored",
  "style_score": 0.2999
}
```

**An appeal**

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"83627415-6d70-4e9f-a74c-190408966f51","reasoning":"I wrote this email myself to explain my absence and request more time."}'
```

```json
{
  "content_id": "83627415-6d70-4e9f-a74c-190408966f51",
  "message": "Your appeal has been recorded for review.",
  "status": "under_review"
}
```

**What the log showed after the first appeal**

This output was captured immediately after the first appeal,
before the later repeated appeal and label tests.

```bash
curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.48465,
      "content_id": "83627415-6d70-4e9f-a74c-190408966f51",
      "creator_id": "calibration-formal-human",
      "guess": "unsure",
      "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
      "model_score": 0.6694,
      "status": "scored",
      "style_score": 0.2999,
      "timestamp": "2026-11-05T01:30:49+00:00"
    },
    {
      "content_id": "83627415-6d70-4e9f-a74c-190408966f51",
      "creator_id": "calibration-formal-human",
      "event": "appeal",
      "reasoning": "I wrote this email myself to explain my absence and request more time.",
      "status": "under_review",
      "timestamp": "2026-11-05T01:36:01+00:00"
    }
  ]
}
```
---

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
