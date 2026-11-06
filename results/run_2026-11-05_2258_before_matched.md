# Run log — before_matched

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-05 22:58

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives |  |   |   |   |  |
| 2. Score separation |  |   |   |   |  |
| 3. Label coverage |  |   |   |   |  |
| 5. Invalid submit requests |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### False positives

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  }
]
```

### Score separation

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48414999999999997,
    "model_score": 0.4683,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I created a little program that assigns an AI-likelihood score to a pi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52545,
    "model_score": 0.5509,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "The resume form contained my email address, but the PDF did not. In or"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4477,
    "model_score": 0.2228,
    "style_score": 0.6726,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I used the same creator ID to send fifteen requests. The next five res"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4357,
    "model_score": 0.3714,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "It was difficult for me to distinguish between a hot take and an analy"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.50135,
    "model_score": 0.5027,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "In one terminal, I launch the Flask application and let it run. In ord"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5645,
    "model_score": 0.629,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hello, I got stuck setting up the test files while working on the next"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5506,
    "model_score": 0.6012,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I spent some time working at the library after lunch. My laptop batter"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31995,
    "model_score": 0.1399,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I kept looking up the room number before entering class throughout my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.47809999999999997,
    "model_score": 0.4562,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "If someone's writing is flagged by a detector, they ought to be given "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34195,
    "model_score": 0.1839,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "I attempted to request something that wasn't in the lists while testin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

### Label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45699999999999996,
    "model_score": 0.414,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I walked to the library after lunch."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2887,
    "model_score": 0.0774,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "The workshop starts at nine tomorrow morning."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3891,
    "model_score": 0.2782,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "We fixed the bug and tested the form again."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45699999999999996,
    "model_score": 0.414,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I walked to the library after lunch."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2887,
    "model_score": 0.0774,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "The workshop starts at nine tomorrow morning."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3891,
    "model_score": 0.2782,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "We fixed the bug and tested the form again."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45699999999999996,
    "model_score": 0.414,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I walked to the library after lunch."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2887,
    "model_score": 0.0774,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "The workshop starts at nine tomorrow morning."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3891,
    "model_score": 0.2782,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "We fixed the bug and tested the form again."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.41575,
    "model_score": 0.3315,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I built a small app that gives a piece of writing an AI-likelihood sco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5731999999999999,
    "model_score": 0.6464,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "My email address showed up in the resume form, but it was missing from"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4698,
    "model_score": 0.3126,
    "style_score": 0.627,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I sent fifteen requests using the same creator ID. The first ten went "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4289,
    "model_score": 0.3578,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I had trouble deciding whether a comment was analysis or a hot take. I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5502,
    "model_score": 0.6004,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "I start the Flask app in one terminal and leave it running. Then I ope"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48760000000000003,
    "model_score": 0.4752,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "Hi, I\u2019m working on the next part of the assignment and got stuck setti"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5844,
    "model_score": 0.6688,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "After lunch, I went to the library to work for a while. I spent the fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851999999999999,
    "model_score": 0.6704,
    "style_score": 0.5,
    "label": "Our automated checks cannot confidently determine how this text was created. This uncertainty is not an accusation. You can request a review.",
    "sent": "During my first week, I kept checking the room number before walking i"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34445000000000003,
    "model_score": 0.1889,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "If a detector flags someone\u2019s writing, the writer should have a chance"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.32,
    "model_score": 0.14,
    "style_score": 0.5,
    "label": "Our automated checks suggest this text was written by a person. This result is not proof of authorship.",
    "sent": "While testing FitFindr, I tried asking for something that wasn\u2019t in th"
  }
]
```

### Invalid submit requests

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_number_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This request has no creator ID.\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has an empty creator ID."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has a numeric creator ID."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_number_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This request has no creator ID.\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has an empty creator ID."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has a numeric creator ID."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_number_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This request has no creator ID.\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has an empty creator ID."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "This request has a numeric creator ID."
  }
]
```
