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

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

**A submission**

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"I think the  us congres will be fliped by the democrats for this us midterm 2026.","creator_id":"patrick"}'
```

```json
{
  "confidence": null,
  "content_id": "4e4032b2-ac91-49be-87f0-18fb571094c9",
  "guess": "human",
  "label": "Model signal only. Final scoring and labels are not connected.",
  "model_score": 0.028,
  "status": "scored",
  "style_score": null
}
```

**An appeal**

Not implemented yet. The request, response, and audit log
evidence will be added in Milestone 5.

**What the log shows afterwards**

```bash
curl "http://127.0.0.1:5000/log?limit=1"
```

```json
{
  "count": 1,
  "entries": [
    {
      "combined_score": null,
      "content_id": "4e4032b2-ac91-49be-87f0-18fb571094c9",
      "creator_id": "patrick",
      "guess": "human",
      "label": "Model signal only. Final scoring and labels are not connected.",
      "model_score": 0.028,
      "status": "scored",
      "style_score": null,
      "timestamp": "2026-11-04T02:59:13+00:00"
    }
  ]
}
```


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
