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

# Self-Test: TEI Encoding

````{admonition} Note
:class: note
This assessment helps you check your understanding of the chapter *Corpus Building in DraCor*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, even if you answered correctly.
- If you are unsure, return to the relevant section of the chapter (or the interface/tool) and verify what you see.

<!-- TODO: the following information needs to be checked. -->
Estimated time: 10–20 minutes.
````

## Exercise 1: Imported and In-house Corpora

Determine if a corpus has been imported, built in-house, or follows a mixed approach as of 2026.

<!-- TODO: Discuss corpus type of German Drama Corpus – mixed/in-house (feedback: It started as an imported corpus, but is now extended in-house.)-->

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "French Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": True, "feedback": "Correct!"},
      {"answer": "in-house", "correct": False,  "feedback": "Incorrect."},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [
  {
    "question": "Polish Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": False, "feedback": "Incorrect."},
      {"answer": "in-house", "correct": True,  "feedback": "Correct!"},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [
  {
    "question": "English Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": True, "feedback": "Correct!"},
      {"answer": "in-house", "correct": False,  "feedback": "Incorrect."},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [
  {
    "question": "Italian Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": False, "feedback": "Incorrect."},
      {"answer": "in-house", "correct": False,  "feedback": "Incorrect."},
      {"answer": "mixed", "correct": True, "feedback": "Correct!"}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [
  {
    "question": "Ukrainian Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": False, "feedback": "Incorrect."},
      {"answer": "in-house", "correct": True,  "feedback": "Correct!"},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [
  {
    "question": "Ibsen Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": True, "feedback": "Correct!"},
      {"answer": "in-house", "correct": False,  "feedback": "Incorrect."},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [
  {
    "question": "Russian Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": False, "feedback": "Incorrect."},
      {"answer": "in-house", "correct": True,  "feedback": "Correct!"},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q8 = [
  {
    "question": "Dutch Drama Corpus",
    "type": "multiple_choice",
    "answers": [
      {"answer": "imported", "correct": False, "feedback": "Incorrect."},
      {"answer": "in-house", "correct": True,  "feedback": "Correct!"},
      {"answer": "mixed", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

## Exercise 2: Selection Criteria in Corpus Building

Assign the corpus building criteria to the DraCor corpora. Select the **primary selection criterion** for each corpus. You may select up to two primary selection criteria per corpus.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "Ibsen Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": True, "feedback": "Correct!"}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [
  {
    "question": "German Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct!"},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [
  {
    "question": "Greek Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "period focus", "correct": True,  "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [
  {
    "question": "Calderon Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": True, "feedback": "Correct!"}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [
  {
    "question": "Russian Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct!"},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [
  {
    "question": "Romanian Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct!"},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [
  {
    "question": "Shakespeare Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": True, "feedback": "Correct!"}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q8 = [
  {
    "question": "Hungarian Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct!"},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q9 = [
  {
    "question": "Argentinian Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": True, "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q10 = [
  {
    "question": "Roman Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "period focus", "correct": True,  "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q11 = [
  {
    "question": "Neo-Latin Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "period focus", "correct": True,  "feedback": "Correct! Note that this corpus has two focuses."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q12 = [
  {
    "question": "Polish Drama Corpus",
    "type": "many_choice",
    "answers": [
      {"answer": "language focus", "correct": True, "feedback": "Correct!"},
      {"answer": "period focus", "correct": False,  "feedback": "Incorrect."},
      {"answer": "region focus", "correct": False, "feedback": "Incorrect."},
      {"answer": "author focus", "correct": False, "feedback": "Incorrect."}
    ]
  }
]

display_quiz(q1, max_width=1000)
```