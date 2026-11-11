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

# Self-Test: Infrastructure

::::{admonition} Note
:class: note
This self-test helps you check your understanding of the chapter *DraCor in the Context of Research Infrastructures*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- If you are unsure, return to the relevant section of the chapter.

Estimated time: 15–20 minutes.
::::

## Question 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [{
  "question": "How does the chapter characterise the way DraCor became an infrastructure?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "As a tactical infrastructure that grew bottom-up from a specific research need into a multi-component system.", "correct": True,
     "feedback": "Correct. DraCor grew from network analysis of drama; CLS INFRA adopted this idea of tactical infrastructure (section 4.1)."},
    {"answer": "As a European Research Infrastructure Consortium (ERIC), like CLARIN and DARIAH.", "correct": False,
     "feedback": "No. The chapter contrasts DraCor with the large, centrally organised ERICs."},
    {"answer": "As a commercial platform that was later opened to researchers.", "correct": False,
     "feedback": "No. DraCor is an open-source project from the start, maintained by researchers."},
    {"answer": "As a single application that was designed completely before it was built.", "correct": False,
     "feedback": "No. DraCor is a system of several components that evolved over time."}
  ]
}]
display_quiz(q1, max_width=1000)
```

## Question 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [{
  "question": "DraCor has no full-text search. What does the chapter take this as an example of?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Of how an infrastructure reflects the needs it grew from: the API is designed around corpus and play, for extracting structured data rather than searching.", "correct": True,
     "feedback": "Correct. The missing search is a window into the design of the infrastructure, and an invitation to develop it further (section 4.1)."},
    {"answer": "Of a technical limitation of XML databases, which cannot search text.", "correct": False,
     "feedback": "No. eXist-db can search text; full-text search was simply not part of DraCor's design."},
    {"answer": "Of a legal restriction on the texts.", "correct": False,
     "feedback": "No. The corpora are openly licensed; the reason lies in the design of the system."},
    {"answer": "Of a bug that will be fixed in the next version.", "correct": False,
     "feedback": "No. It is not a bug but a consequence of what the system was built for."}
  ]
}]
display_quiz(q2, max_width=1000)
```

## Question 3

Match each component of the DraCor system with its role (section 4.2).

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from assessment import DragDropQuiz

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="Components of the DraCor system",
    descriptions=[
        "Corpus repositories on GitHub",
        "eXist-db with the DraCor API",
        "Metrics Service",
        "Front-end",
        "Triple Store",
    ],
    options=[
        "Hold the TEI source files under version control",
        "Stores the plays and answers API requests, written in XQuery",
        "Calculates the network metrics of each play, written in Python",
        "React application in the browser that calls the API",
        "Holds RDF data and offers a SPARQL endpoint",
    ],
    correct_mapping={
        "Corpus repositories on GitHub": "Hold the TEI source files under version control",
        "eXist-db with the DraCor API": "Stores the plays and answers API requests, written in XQuery",
        "Metrics Service": "Calculates the network metrics of each play, written in Python",
        "Front-end": "React application in the browser that calls the API",
        "Triple Store": "Holds RDF data and offers a SPARQL endpoint",
    },
)
```

## Question 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [{
  "question": "When are the network metrics of a play (for example density or diameter) calculated?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "When the play is loaded: the API sends the network to the Metrics Service, and the results are stored in the database.", "correct": True,
     "feedback": "Correct. The metrics are pre-calculated during the ingest and then served by the API."},
    {"answer": "Each time someone requests the /metrics endpoint.", "correct": False,
     "feedback": "No. The metrics are calculated once, when the play is loaded, and then stored."},
    {"answer": "In the browser, by the front-end.", "correct": False,
     "feedback": "No. The front-end only displays the metrics it receives from the API."},
    {"answer": "By the corpus editors, who enter them in the TEI files.", "correct": False,
     "feedback": "No. The TEI files contain the play; the metrics are computed from its structure."}
  ]
}]
display_quiz(q4, max_width=1000)
```

## Question 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [{
  "question": "You analysed a corpus on dracor.org a year ago. Why might you not get the same results today?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because DraCor corpora are living corpora: plays are added, corrected or re-encoded, without notice to users.", "correct": True,
     "feedback": "Correct. This is why controlling the data version matters for reproducibility (section 5.1)."},
    {"answer": "Because the API deletes old data after one year.", "correct": False,
     "feedback": "No. Nothing is deleted on a schedule; the corpora change as they are curated."},
    {"answer": "Because results on dracor.org are randomised.", "correct": False,
     "feedback": "No. The same data and software give the same results; the data, however, may have changed."},
    {"answer": "Because only the front-end changes, never the data.", "correct": False,
     "feedback": "No. Both the software and the data can change."}
  ]
}]
display_quiz(q5, max_width=1000)
```

## Question 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [{
  "question": "What is the difference between a Docker image and a container?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "An image is a frozen snapshot of an application and everything it needs; a container is a running copy of an image.", "correct": True,
     "feedback": "Correct (section 5.2)."},
    {"answer": "An image is a screenshot of the front-end; a container is the database.", "correct": False,
     "feedback": "No. Both terms refer to software packaging, not to parts of DraCor."},
    {"answer": "There is no difference; both words mean the same.", "correct": False,
     "feedback": "No. You start a container from an image, and you can run several containers from the same image."},
    {"answer": "A container is a file on Docker Hub; an image runs on your computer.", "correct": False,
     "feedback": "It is the other way round: images are published on Docker Hub, containers run on your computer."}
  ]
}]
display_quiz(q6, max_width=1000)
```

## Question 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [{
  "question": "You want a colleague to run exactly the same DraCor setup as you. What do you share, given that the images are published on Docker Hub?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "A Compose file that specifies exact image versions.", "correct": True,
     "feedback": "Correct. With exact versions (for example dracor/api:1.4.1 instead of latest), docker compose up starts the same system elsewhere (section 5.2)."},
    {"answer": "A Compose file that uses the tag latest for all images.", "correct": False,
     "feedback": "Not reliable: latest points to whatever version is newest when your colleague runs it."},
    {"answer": "A screenshot of the running front-end.", "correct": False,
     "feedback": "No. A screenshot documents what you saw, but nobody can run it."},
    {"answer": "Nothing; everybody gets the same setup from dracor.org anyway.", "correct": False,
     "feedback": "No. dracor.org changes over time; a local setup is shared through the Compose file."}
  ]
}]
display_quiz(q7, max_width=1000)
```

## Question 8

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q8 = [{
  "question": "How do you load a corpus into your local DraCor instance?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Register the corpus by sending its corpus.xml to the API, then trigger the loading of the plays; both through admin endpoints.", "correct": True,
     "feedback": "Correct. Locally you can use the admin endpoints, because you set the password yourself (section 5.4)."},
    {"answer": "Copy the TEI files into the front-end folder.", "correct": False,
     "feedback": "No. Corpora are loaded through the API, which stores them in eXist-db."},
    {"answer": "Download the corpus from the dracor.org front-end and open it in the browser.", "correct": False,
     "feedback": "No. That gives you files, but does not load them into your instance."},
    {"answer": "It is not possible; a local instance can only show the corpora of dracor.org.", "correct": False,
     "feedback": "No. You can load any DraCor-compatible corpus from GitHub, and your own TEI files."}
  ]
}]
display_quiz(q8, max_width=1000)
```

## Question 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q9 = [{
  "question": "You put your own DraCor online on the EOSC EU Node and load a corpus from GitHub. What does this give you, and what not?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "An instance others can access, useful for teaching, demos or sharing a custom corpus; but it holds the current state of the corpus and does not by itself freeze data and software.", "correct": True,
     "feedback": "Correct. For reproducibility you still need to fix the versions, for example with a committed image (section 5.5)."},
    {"answer": "A permanent, citable archive of the corpus.", "correct": False,
     "feedback": "No. A running instance is not an archive; for a citable version, use a repository with a DOI."},
    {"answer": "A copy of dracor.org that updates itself.", "correct": False,
     "feedback": "No. Your instance has the data you loaded; it does not follow changes on dracor.org."},
    {"answer": "Only a local instance that nobody else can reach.", "correct": False,
     "feedback": "No. That is the difference to a local instance: an instance on the EU Node has a public address."}
  ]
}]
display_quiz(q9, max_width=1000)
```
