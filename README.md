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
AI-generated. This result can be wrong. You can request a review."

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

**What it measures:** GPT-2 measures text predictability using
perplexity. detector.py converts this into a score from 0 to 1.
Lower perplexity produces a higher AI-likelihood score.

**Why that might differ between human and AI writing:**
AI-generated text may use predictable wording, but human writing
can also be predictable. This is an experimental clue.

**What it can't see:** It cannot verify authorship or the writing
process. Plain or conventional human writing may score highly,
while unusual wording or edited AI writing may score lower.

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
**Moment 1 — Connecting the signals**

- *What I asked for:* I asked ChatGPT to help connect the model
  and style signals to my submission endpoint.
- *What came back:* It provided code to calculate both scores,
  combine them, and save the results in the audit log.
- *What I changed:* After getting a model_score NameError,
  I used its guidance to restore the detector call before
  combining the scores. I reran the request and checked that
  all three scores appeared in the audit log.

**Moment 2 — Building and testing the style signal**

- *What I asked for:* I asked ChatGPT for help implementing
  the style signal using the starter files.
- *What came back:* It supplied functions for sentence length
  variation, word variety, and punctuation density, with an
  experimental rule for combining them.
- *What I changed:* I replaced the starter stubs with the
  suggested implementation and removed the outdated stub
  message. During testing, I corrected sentence spacing in
  my sample so the splitter recognized three sentences.
  I documented the actual results, including cases where
  the two signals disagreed on my human-written text.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

I set the submission limits to 10 requests per minute and 200 per day
per creator ID, falling back to the caller's address when no usable
creator ID is provided. These limits allow a writer to check several
pieces while slowing automated attempts to probe the detector.

The 15-request flood test returned:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Ten requests succeeded and five were rate limited. I also tested an
empty-text submission: it returned HTTP 400 and created an audit entry
with reason `invalid_text`.

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

I ran all 56 staff attack rows with `python run_attacks.py --set attack_set` before changing the detector. The baseline produced 36 HELD and 20 BROKE under the rules below. There were no server errors.

| Family | HELD | BROKE |
|---|---:|---:|
| Evasion | 1 | 9 |
| False positive | 2 | 6 |
| Prompt injection | 6 | 0 |
| Malformed | 15 | 5 |
| Flood, same creator | 12 | 0 |

- **Evasion:** HELD if the detector returned `ai`. I count `unsure` as successful evasion because the input avoided the AI flag.
- **False positive:** BROKE if human writing was flagged as `ai`.
- **Prompt injection:** HELD when the record showed a normal scored response, standard label, and matching audit entry. PI02 returned `human`, so its verdict is provisional. A normal audit record alone cannot show whether its wording influenced the score.
- **Malformed:** HELD if an invalid request received `400`. I also count MF07 as HELD for request handling because right-to-left writing is valid text. The `ai` label on MF07 does not establish authorship.
- **Flood:** HELD if the response matched the configured cutoff. The runner executed 12 flood rows, even though the targeting description says 20. It accepted the first 10 and rejected the next two with `429`.

The per-signal scores below come from audit entries matched by content ID.

| ID | Family | Targeting | HTTP | Content ID | Guess | Combined | Model | Style | Verdict |
|---|---|---|---:|---|---|---:|---:|---:|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `313fd4c8-1368-42bc-8c24-a0cf4ab41565` | unsure | 0.392 | 0.1635 | 0.6201 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f17dec9f-ec4f-4e58-8e69-e616b4e64728` | unsure | 0.434 | 0.5943 | 0.273 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5f684d09-a0e0-4395-8a04-ddd8d31b1ee9` | unsure | 0.567 | 0.6662 | 0.4668 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5895fa6f-defe-4940-86e0-f3e20b81c19d` | unsure | 0.611 | 0.6114 | 0.6096 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `ae652fbf-50e4-4aba-8f2b-212517469e61` | human | 0.340 | 0.3212 | 0.3582 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `da9a23b0-3e68-494d-9e21-550cd8500fb3` | unsure | 0.409 | 0.5727 | 0.2459 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `98a1ff5b-c3e8-4fbd-b684-77c161d5e1fc` | unsure | 0.543 | 0.5862 | 0.5 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `39bb234d-dc3b-4fa3-aa9b-ede6d09d3564` | unsure | 0.373 | 0.2452 | 0.5 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `909a93a3-3b0e-4985-9bb4-1c3cb65c00ba` | unsure | 0.581 | 0.7042 | 0.4575 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f762e535-c046-4be9-9d35-f1989c15a7ce` | ai | 0.837 | 0.9792 | 0.694 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4460a6d4-4a15-4a60-9d53-f58ff055055e` | unsure | 0.564 | 0.6175 | 0.5111 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `ac400aae-7972-4de6-8fd1-a2cacd14bfb1` | ai | 0.683 | 0.7387 | 0.6269 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `dc6a5abf-0a64-4c2c-a2ec-d78ce1fb6613` | ai | 0.691 | 0.8051 | 0.5774 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b6df1894-05c7-4064-9702-168da286b6dd` | ai | 0.679 | 0.8329 | 0.5261 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `fadd8bd4-f26a-42ff-b68c-fa63e612c4e9` | ai | 0.715 | 0.8005 | 0.6303 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `0d9a00bf-4f1f-452f-b683-77125bdcbd66` | ai | 0.677 | 0.8814 | 0.4718 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `93babadb-8fbc-4620-86e4-58945962f836` | ai | 0.657 | 0.8816 | 0.4323 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `715fa1fa-ce7a-47c7-896d-c0b280e7df18` | unsure | 0.411 | 0.3223 | 0.5 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b68424e4-8699-4d8f-9042-4983cf185f86` | unsure | 0.407 | 0.4625 | 0.3524 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5baa5bc4-d571-4d4e-9279-b1ce3c9560e8` | human | 0.267 | 0.2044 | 0.3303 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `cb98bace-a03f-43bf-b712-373a9e2b3ffb` | unsure | 0.553 | 0.5943 | 0.5123 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `da763580-886a-4c1e-a052-5d896fe12ef8` | unsure | 0.482 | 0.4998 | 0.4642 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `192d2487-cb3b-4239-ab25-8af4bab5968e` | unsure | 0.570 | 0.6401 | 0.5 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `93a10adb-9034-48ed-9a2b-90d348f4a692` | unsure | 0.539 | 0.5583 | 0.5191 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `3b512dea-5d56-4a78-8705-3eccf14fb356` | human | 0.250 | 0.0 | 0.5 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `57a9f22b-5a54-499a-8fc1-2c0c236c18f2` | human | 0.256 | 0.0112 | 0.5 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `a532580e-e074-4ff4-a102-0d52ab73cd44` | ai | 0.749 | 0.9976 | 0.5 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `9341f96b-3470-40e4-9f7a-1ec4b578e798` | ai | 0.748 | 0.9969 | 0.5 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `846a2edd-0d53-45db-9e43-4fc0bb3f9c50` | ai | 0.703 | 0.9064 | 0.5 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `498e79b8-4c2c-4143-856f-9fa477550c64` | ai | 0.862 | 0.9876 | 0.7365 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5abd03b2-44d6-443e-848b-5f9edf7f4d66` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `57fe1850-3c2e-4150-ada2-64055fb0e0ba` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `abf526c4-d525-48d8-bd15-7ca46cbfe29b` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3f885841-e323-4062-9bde-de00f234f378` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4c979424-1c68-4f08-af15-f75f009fc86f` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0aa5c471-3265-4de0-8261-bcdd53f353e2` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `95362a4c-79e7-4d10-be40-2dce46dd5b04` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c000f929-231f-4ad7-a010-d77dc1ff4d4c` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e605ad56-fe1e-4372-9efa-a593dde085f5` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `62c4e713-61a2-4818-ae82-c8b7db262487` | human | 0.264 | 0.0287 | 0.5 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | — | — | HELD |

### Worst outcome

FP05 flagged human-written technical documentation as AI with a combined score of 0.715. It had the highest score among the human samples flagged as AI in this run. A writer could have their work wrongly questioned based on that result.

### Audit evidence

These ten entries come from the baseline run. The final entry records one of the two flood rejections.

```jsonl
{"combined_score": 0.3918, "content_id": "313fd4c8-1368-42bc-8c24-a0cf4ab41565", "creator_id": "attacker_EV01", "guess": "unsure", "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.", "model_score": 0.1635, "status": "scored", "style_score": 0.6201, "timestamp": "2026-11-06T00:48:26+00:00"}
{"combined_score": 0.3397, "content_id": "ae652fbf-50e4-4aba-8f2b-212517469e61", "creator_id": "attacker_EV05", "guess": "human", "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.", "model_score": 0.3212, "status": "scored", "style_score": 0.3582, "timestamp": "2026-11-06T00:48:27+00:00"}
{"combined_score": 0.6828000000000001, "content_id": "ac400aae-7972-4de6-8fd1-a2cacd14bfb1", "creator_id": "attacker_FP02", "guess": "ai", "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.", "model_score": 0.7387, "status": "scored", "style_score": 0.6269, "timestamp": "2026-11-06T00:48:29+00:00"}
{"combined_score": 0.69125, "content_id": "dc6a5abf-0a64-4c2c-a2ec-d78ce1fb6613", "creator_id": "attacker_FP03", "guess": "ai", "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.", "model_score": 0.8051, "status": "scored", "style_score": 0.5774, "timestamp": "2026-11-06T00:48:29+00:00"}
{"combined_score": 0.7154, "content_id": "fadd8bd4-f26a-42ff-b68c-fa63e612c4e9", "creator_id": "attacker_FP05", "guess": "ai", "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.", "model_score": 0.8005, "status": "scored", "style_score": 0.6303, "timestamp": "2026-11-06T00:48:29+00:00"}
{"combined_score": 0.26735, "content_id": "5baa5bc4-d571-4d4e-9279-b1ce3c9560e8", "creator_id": "attacker_PI02", "guess": "human", "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.", "model_score": 0.2044, "status": "scored", "style_score": 0.3303, "timestamp": "2026-11-06T00:48:30+00:00"}
{"combined_score": 0.482, "content_id": "da763580-886a-4c1e-a052-5d896fe12ef8", "creator_id": "attacker_PI04", "guess": "unsure", "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.", "model_score": 0.4998, "status": "scored", "style_score": 0.4642, "timestamp": "2026-11-06T00:48:31+00:00"}
{"combined_score": 0.57005, "content_id": "192d2487-cb3b-4239-ab25-8af4bab5968e", "creator_id": "attacker_PI05", "guess": "unsure", "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.", "model_score": 0.6401, "status": "scored", "style_score": 0.5, "timestamp": "2026-11-06T00:48:31+00:00"}
{"combined_score": 0.86205, "content_id": "498e79b8-4c2c-4143-856f-9fa477550c64", "creator_id": "attacker_MF08", "guess": "ai", "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.", "model_score": 0.9876, "status": "scored", "style_score": 0.7365, "timestamp": "2026-11-06T00:48:34+00:00"}
{"creator_id": "attacker_flood", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-06T00:48:35+00:00"}
```
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
