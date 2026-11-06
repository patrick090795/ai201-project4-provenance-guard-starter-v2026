# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 22:47
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `42a5c731-a7e8-4871-992c-64f3bacac034` | unsure | 0.392 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `6dea3c93-37db-45be-b446-0d00cb451d58` | unsure | 0.434 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cd6057d8-396e-4bba-ac4c-37312a272a80` | unsure | 0.567 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d65072c4-edb9-49c1-b53a-2a63a4cf58ac` | unsure | 0.611 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bc95e517-337a-4a3e-9749-d5f123c9a4e1` | human | 0.340 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b7d61e29-5c3d-4cda-8a79-a4803199a525` | unsure | 0.409 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `224b2e3f-22ae-4c6d-b025-084980aec6f5` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `85641e73-c16b-44c4-bae8-77e3fcd54497` | unsure | 0.373 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5a144750-3a15-420c-b5c5-c8e5137e2d46` | unsure | 0.581 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c202e781-0369-4c5d-bf92-af0402fe24f9` | ai | 0.837 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9fc5584e-ef20-4bb2-93ba-654bca38b1c5` | unsure | 0.564 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `b53490e3-ceeb-4082-bc1f-8bf0dc7c5d30` | unsure | 0.683 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `224667e2-831a-4dcb-995b-9cf88b769397` | unsure | 0.691 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `71741416-90c1-4b01-a638-be0ae432908e` | unsure | 0.679 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `8b25ad75-53ab-482e-b2e6-316e6e61131f` | unsure | 0.715 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `1064356b-27ac-4715-b6f1-688d5e699e8d` | unsure | 0.677 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `bf13de6a-f63f-49ab-b08e-921af9961320` | unsure | 0.657 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2f4a6cbc-3a1b-4f22-b4e6-ee79b6250804` | unsure | 0.411 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c32704fa-c6c6-44f1-bced-518cb0dcf8ca` | unsure | 0.407 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `10cb0802-2d03-46a1-aabc-e449b2f6dc97` | human | 0.267 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `71c6a736-b88d-4828-b077-d1ee8386371a` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d2e08b79-0109-4011-955c-1abd154ccab6` | unsure | 0.482 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `43676845-d29e-4f63-a80c-48b26a7ea5bc` | unsure | 0.570 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b59693e4-9b2f-4e9f-8c71-48d715e18f4d` | unsure | 0.539 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `89985870-409c-4fe6-95c7-da66718e4184` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `8d4d90df-2864-4c78-a805-8af03382bde9` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `61c9be74-a114-4e8f-a221-57026a2d3fe3` | ai | 0.749 |  |
| MF06 | malformed | text is emoji only | 200 | `b5a38006-189b-4661-bd19-b3adcac5b52b` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `97fe3a16-2fb7-48b1-b917-346f14ac9431` | unsure | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `2bcf1c88-7974-48f8-a1c2-8d4393c9621a` | ai | 0.862 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `41f63ce3-4ef9-4dcd-a14b-44272ba441a8` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `49fffd8f-2129-41c8-95c7-46a4142aa181` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `63663c97-8ace-4dbd-b06d-a68b656f376d` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a29ae7ed-4b9a-467e-9298-1ff4510b8d21` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2294eb72-5ad8-43a9-a21d-baaf4646e3c3` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `107ad263-665a-45b3-a513-942d0551e3b3` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32e614fd-244c-4cf0-bf51-e9b7b55fb757` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `317572d6-ba46-4351-9e77-f762a1cf71a9` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d7ba97d-ed0d-4f1b-8729-b843b4f13f9f` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `206dea3a-7132-4d83-b21b-a62ba7c13e68` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "42a5c731-a7e8-4871-992c-64f3bacac034",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3918,
  "model_score": 0.1635,
  "style_score": 0.6201,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "6dea3c93-37db-45be-b446-0d00cb451d58",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.43365000000000004,
  "model_score": 0.5943,
  "style_score": 0.273,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "cd6057d8-396e-4bba-ac4c-37312a272a80",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5665,
  "model_score": 0.6662,
  "style_score": 0.4668,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d65072c4-edb9-49c1-b53a-2a63a4cf58ac",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6105,
  "model_score": 0.6114,
  "style_score": 0.6096,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bc95e517-337a-4a3e-9749-d5f123c9a4e1",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3397,
  "model_score": 0.3212,
  "style_score": 0.3582,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "b7d61e29-5c3d-4cda-8a79-a4803199a525",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4093,
  "model_score": 0.5727,
  "style_score": 0.2459,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "224b2e3f-22ae-4c6d-b025-084980aec6f5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "85641e73-c16b-44c4-bae8-77e3fcd54497",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3726,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "5a144750-3a15-420c-b5c5-c8e5137e2d46",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5808500000000001,
  "model_score": 0.7042,
  "style_score": 0.4575,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c202e781-0369-4c5d-bf92-af0402fe24f9",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8366,
  "model_score": 0.9792,
  "style_score": 0.694,
  "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9fc5584e-ef20-4bb2-93ba-654bca38b1c5",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5643,
  "model_score": 0.6175,
  "style_score": 0.5111,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "b53490e3-ceeb-4082-bc1f-8bf0dc7c5d30",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6828000000000001,
  "model_score": 0.7387,
  "style_score": 0.6269,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "224667e2-831a-4dcb-995b-9cf88b769397",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.69125,
  "model_score": 0.8051,
  "style_score": 0.5774,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "71741416-90c1-4b01-a638-be0ae432908e",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6795,
  "model_score": 0.8329,
  "style_score": 0.5261,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "8b25ad75-53ab-482e-b2e6-316e6e61131f",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7154,
  "model_score": 0.8005,
  "style_score": 0.6303,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "1064356b-27ac-4715-b6f1-688d5e699e8d",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6766,
  "model_score": 0.8814,
  "style_score": 0.4718,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "bf13de6a-f63f-49ab-b08e-921af9961320",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.65695,
  "model_score": 0.8816,
  "style_score": 0.4323,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "2f4a6cbc-3a1b-4f22-b4e6-ee79b6250804",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.41115,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c32704fa-c6c6-44f1-bced-518cb0dcf8ca",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.40745,
  "model_score": 0.4625,
  "style_score": 0.3524,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "10cb0802-2d03-46a1-aabc-e449b2f6dc97",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.26735,
  "model_score": 0.2044,
  "style_score": 0.3303,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "71c6a736-b88d-4828-b077-d1ee8386371a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5533,
  "model_score": 0.5943,
  "style_score": 0.5123,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d2e08b79-0109-4011-955c-1abd154ccab6",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.482,
  "model_score": 0.4998,
  "style_score": 0.4642,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "43676845-d29e-4f63-a80c-48b26a7ea5bc",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.57005,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "b59693e4-9b2f-4e9f-8c71-48d715e18f4d",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5387,
  "model_score": 0.5583,
  "style_score": 0.5191,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "89985870-409c-4fe6-95c7-da66718e4184",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "8d4d90df-2864-4c78-a805-8af03382bde9",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "61c9be74-a114-4e8f-a221-57026a2d3fe3",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "b5a38006-189b-4661-bd19-b3adcac5b52b",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7484500000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "97fe3a16-2fb7-48b1-b917-346f14ac9431",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "2bcf1c88-7974-48f8-a1c2-8d4393c9621a",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.86205,
  "model_score": 0.9876,
  "style_score": 0.7365,
  "label": "Our automated checks suggest this text may be AI-generated. This result can be wrong. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "41f63ce3-4ef9-4dcd-a14b-44272ba441a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "49fffd8f-2129-41c8-95c7-46a4142aa181",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "63663c97-8ace-4dbd-b06d-a68b656f376d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "a29ae7ed-4b9a-467e-9298-1ff4510b8d21",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "2294eb72-5ad8-43a9-a21d-baaf4646e3c3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "107ad263-665a-45b3-a513-942d0551e3b3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "32e614fd-244c-4cf0-bf51-e9b7b55fb757",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "317572d6-ba46-4351-9e77-f762a1cf71a9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "7d7ba97d-ed0d-4f1b-8729-b843b4f13f9f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "206dea3a-7132-4d83-b21b-a62ba7c13e68",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
