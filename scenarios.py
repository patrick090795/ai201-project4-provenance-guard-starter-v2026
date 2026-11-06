"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""
WRITING_SAMPLES = [
    "I spent some time working at the library after lunch. My laptop battery was low, so I spent the first few minutes searching for a seat close to an outlet.",
    "I kept looking up the room number before entering class throughout my first week. Finding the entrance nearest to my classroom took several days.",
    "If someone's writing is flagged by  detector, they ought to be given an opportunity to clarify how they produced it. The way a teacher or reviewer handles their work can be impacted by the incorrect flag.",
    "I attempted to request something that wasn't in the lists while testing FitFindr. That made it easier for me to see if the agent would pause and describe what transpired rather than recommending an item it hadn't located.",
]

AI_SAMPLES = [
    "I built a small app that gives a piece of writing an AI-likelihood score. It can also say it is unsure, which matters when the evidence is weak.",
    "My email address showed up in the resume form, but it was missing from the PDF. I checked the template first because I wanted to see what happened between filling out the form and downloading the file.",
    "I sent fifteen requests using the same creator ID. The first ten went through, and the next five returned HTTP 429. I checked the audit log and found all five rejections.",
    "I had trouble deciding whether a comment was analysis or a hot take. I looked for a specific detail that supported the claim, because some comments sounded convincing even when they gave very little evidence.",
    "I start the Flask app in one terminal and leave it running. Then I open another terminal to send requests so I can read the response and still see any errors on the server.",
    "Hi, I’m working on the next part of the assignment and got stuck setting up the test files. Could you tell me which folder they should go in?",
    "After lunch, I went to the library to work for a while. I spent the first few minutes looking for a seat near an outlet because my laptop battery was low.",
    "During my first week, I kept checking the room number before walking into class. It took me a few days to learn which entrance was closest to my classroom.",
    "If a detector flags someone’s writing, the writer should have a chance to explain how they wrote it. A wrong flag can affect how a teacher or reviewer treats their work.",
    "While testing FitFindr, I tried asking for something that wasn’t in the listings. That helped me check whether the agent would stop and explain what happened instead of suggesting an item it hadn’t found.",
]

SCENARIOS = [
    {
        "name": "False positives",
        "criterion": 1,
        "texts": WRITING_SAMPLES,
    },
    {
        # Positions 1–10 are your samples. Positions 11–20 are AI samples.
        "name": "Score separation",
        "criterion": 2,
        "texts": WRITING_SAMPLES + AI_SAMPLES,
    },
    {
        # Reuse the texts from the Milestone 1 log check and add the AI samples.
        "name": "Label coverage",
        "criterion": 3,
        "texts": [
            "I walked to the library after lunch.",
            "The workshop starts at nine tomorrow morning.",
            "We fixed the bug and tested the form again.",
            *AI_SAMPLES,
        ],
    },
    {
        "name": "Invalid submit requests",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            {"text": 123, "creator_id": "eval_number_text"},
            {"text": "This request has no creator ID."},
            {"text": "This request has an empty creator ID.", "creator_id": ""},
            {"text": "This request has a numeric creator ID.", "creator_id": 123},
        ],
    },
]

def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
