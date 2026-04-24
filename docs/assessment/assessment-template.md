---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Self-test: <CHAPTER SHORT TITLE>

::::{admonition} Note
:class: note
This self-test helps you check your understanding of the chapter *<CHAPTER TITLE>*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- If you are unsure, return to the relevant section of the chapter (or the interface/tool) and verify what you see.

Estimated time: <10–20 minutes>.
::::

## How to use this template (authors)

1. Replace the placeholders in angle brackets: `<...>`.
2. Keep questions aligned with the chapter’s learning outcomes (aim for 6–10 questions).
3. For each multiple-choice question:
   - Provide 3–5 options.
   - Mark exactly one option as `"correct": True` (unless you intentionally use a different type).
   - Provide feedback for every option (including the correct one).
4. Prefer questions that can be verified (by re-running a step, checking the UI, or inspecting outputs).
5. Keep code cells tagged with `remove-input` so learners see the quiz, not the Python source.

## Question 1 (multiple choice)

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "<WRITE YOUR QUESTION HERE>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<Option A>", "correct": False, "feedback": "<Feedback for A>"},
      {"answer": "<Option B>", "correct": True,  "feedback": "<Feedback for B (correct)>"},
      {"answer": "<Option C>", "correct": False, "feedback": "<Feedback for C>"},
      {"answer": "<Option D (optional)>", "correct": False, "feedback": "<Feedback for D>"}
    ]
  }
]

display_quiz(q1, max_width=1000)
:::

## Question 2 (multiple choice)

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [
  {
    "question": "<WRITE YOUR QUESTION HERE>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<Option A>", "correct": False, "feedback": "<Feedback for A>"},
      {"answer": "<Option B>", "correct": True,  "feedback": "<Feedback for B (correct)>"},
      {"answer": "<Option C>", "correct": False, "feedback": "<Feedback for C>"}
    ]
  }
]

display_quiz(q2, max_width=1000)
:::

## Question 3 (multiple choice)

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [
  {
    "question": "<WRITE YOUR QUESTION HERE>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<Option A>", "correct": False, "feedback": "<Feedback for A>"},
      {"answer": "<Option B>", "correct": True,  "feedback": "<Feedback for B (correct)>"},
      {"answer": "<Option C>", "correct": False, "feedback": "<Feedback for C>"}
    ]
  }
]

display_quiz(q3, max_width=1000)
:::

## Question 4 (multiple choice)

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [
  {
    "question": "<WRITE YOUR QUESTION HERE>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<Option A>", "correct": False, "feedback": "<Feedback for A>"},
      {"answer": "<Option B>", "correct": True,  "feedback": "<Feedback for B (correct)>"},
      {"answer": "<Option C>", "correct": False, "feedback": "<Feedback for C>"},
      {"answer": "<Option D (optional)>", "correct": False, "feedback": "<Feedback for D>"}
    ]
  }
]

display_quiz(q4, max_width=1000)
:::

## Question 5 (multiple choice)

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [
  {
    "question": "<WRITE YOUR QUESTION HERE>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<Option A>", "correct": False, "feedback": "<Feedback for A>"},
      {"answer": "<Option B>", "correct": True,  "feedback": "<Feedback for B (correct)>"},
      {"answer": "<Option C>", "correct": False, "feedback": "<Feedback for C>"}
    ]
  }
]

display_quiz(q5, max_width=1000)
:::

## Question 6 (short written task)

<Write a short instruction, e.g. “Pick one example from the chapter and write a reproducible note including …”>

:::{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from assessment import create_answer_box

create_answer_box(
    "<unique-id-for-this-question>",
    rows=6,
    placeholder="<Example: Corpus: … | Play ID: … | Step: … | Observation: …>",
)
:::

::::{admonition} Example answer (for self-check)
:class: tip, dropdown
<Provide a short model answer that shows what “good” looks like, ideally with reproducibility details.>
::::
