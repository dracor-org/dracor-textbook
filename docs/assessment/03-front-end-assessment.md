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

# Self-test: Front-end – Navigating DraCor

````{admonition} Note
:class: note
This self-test helps you check your understanding of the chapter *Front-end: Navigating DraCor*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- If you are unsure, return to the relevant tab in the DraCor interface and verify what you see.

Estimated time: 15–25 minutes.
````

## Question 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [{
  "question": "What do the corpus cards on the DraCor home page primarily help you do?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Edit TEI files directly in the browser", "correct": False,
     "feedback": "No. The front-end is for browsing and exploring, not editing TEI."},
    {"answer": "Get a quick overview of a corpus (scale, token counts by layer, last update)", "correct": True,
     "feedback": "Correct. The cards provide a compact corpus overview and indicate that multiple textual layers exist."},
    {"answer": "Run Gephi analyses without downloading data", "correct": False,
     "feedback": "No. Gephi workflows require exporting network data (or using Gephi Lite), but the cards are not for that."},
    {"answer": "View only stage directions without spoken text", "correct": False,
     "feedback": "No. Layer distinctions exist, but the cards are about corpus-level summaries."}
  ]
}]
display_quiz(q1, max_width=1000)
```

## Question 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [{
  "question": "For reproducible referencing, which identifier is more reliable than the play title?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The play ID (slug) shown in the URL/header", "correct": True,
     "feedback": "Correct. Titles vary across editions and corpora; the play ID is designed to be stable."},
    {"answer": "The approximate word count of the play", "correct": False,
     "feedback": "No. Word counts can change with encoding updates and are not identifiers."},
    {"answer": "The network diameter", "correct": False,
     "feedback": "No. This is a derived metric, not an identifier."},
    {"answer": "The method name in Speech distribution", "correct": False,
     "feedback": "No. Methods are operationalisations for a chart; they do not identify the play."}
  ]
}]
display_quiz(q2, max_width=1000)
```

## Question 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [{
  "question": "How is the co-occurrence network on the Network tab constructed (as stated by the interface)?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Characters are linked if they speak consecutive lines", "correct": False,
     "feedback": "No. That would be a dialogue adjacency model, not co-occurrence."},
    {"answer": "Characters are linked if they appear in the same segment (scene/act segment)", "correct": True,
     "feedback": "Correct. This is why segmentation choices matter for interpretation."},
    {"answer": "Characters are linked only if they share a Wikidata identifier", "correct": False,
     "feedback": "No. Wikidata linking is external metadata, not a network rule."},
    {"answer": "Characters are linked if they share the same sex attribute", "correct": False,
     "feedback": "No. Sex attributes may be displayed, but they do not define edges."}
  ]
}]
display_quiz(q3, max_width=1000)
```

## Question 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [{
  "question": "In the network summary panel, what does 'density' describe?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The proportion of realised connections out of all possible connections", "correct": True,
     "feedback": "Correct. Density ranges between 0 and 1 in simple graphs."},
    {"answer": "The total number of segments in the play", "correct": False,
     "feedback": "No. Segments are reported separately."},
    {"answer": "The length of the longest speech in the play", "correct": False,
     "feedback": "No. That is speech-related, not a network property."},
    {"answer": "The average number of words per character", "correct": False,
     "feedback": "No. That would be speech volume, not density."}
  ]
}]
display_quiz(q4, max_width=1000)
```

## Question 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [{
  "question": "What is the interpretive use of an 'All-in at segment n (at x%)' indicator?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It tells you when the cast is largely introduced in the segmentation", "correct": True,
     "feedback": "Correct. It is a way to describe how quickly the network accumulates its nodes."},
    {"answer": "It tells you which character has the highest degree", "correct": False,
     "feedback": "No. Maximum degree is reported separately."},
    {"answer": "It shows when stage directions become more frequent than dialogue", "correct": False,
     "feedback": "No. That would require token/layer analysis, not this indicator."},
    {"answer": "It indicates that the TEI encoding is complete", "correct": False,
     "feedback": "No. It is a derived network indicator, not an encoding validation."}
  ]
}]
display_quiz(q5, max_width=1000)
```

## Question 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [{
  "question": "Why should you note the selected method in the Speech distribution tab when reporting observations?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because different methods are different operationalisations of 'speech distribution'", "correct": True,
     "feedback": "Correct. Switching methods can change what the chart emphasises, so comparisons require method transparency."},
    {"answer": "Because the method changes the play ID", "correct": False,
     "feedback": "No. The method affects the chart, not identifiers."},
    {"answer": "Because the method changes the TEI source text", "correct": False,
     "feedback": "No. The TEI remains the same; the method changes how data are summarised."},
    {"answer": "Because the method controls whether the Network tab is available", "correct": False,
     "feedback": "No. Tabs are independent views; methods are within Speech distribution."}
  ]
}]
display_quiz(q6, max_width=1000)
```

## Question 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [{
  "question": "Which feature of the Full text tab most directly reveals the segmentation used for derived views?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The Segments panel listing segments and present characters", "correct": True,
     "feedback": "Correct. It makes the segmentation explicit and helps you contextualise network/distribution patterns."},
    {"answer": "The play title in the header", "correct": False,
     "feedback": "No. Titles identify the play but do not show segmentation."},
    {"answer": "The Tools tab layer selector", "correct": False,
     "feedback": "No. That is for routing layers to external tools."},
    {"answer": "The corpus card token counts", "correct": False,
     "feedback": "No. Those are corpus-level summaries, not play segmentation."}
  ]
}]
display_quiz(q7, max_width=1000)
```

## Question 8

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q8 = [{
  "question": "Where do you download artefacts that correspond to the views in the interface (network files, character list, TEI, etc.)?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Network", "correct": False,
     "feedback": "No. Network focuses on visualisation and summary; exports are centralised elsewhere."},
    {"answer": "Downloads", "correct": True,
     "feedback": "Correct. Downloads is the transparency layer for retrieving files in multiple formats."},
    {"answer": "Full text", "correct": False,
     "feedback": "No. Full text is for reading and navigation; downloads are not centralised there."},
    {"answer": "Tools", "correct": False,
     "feedback": "No. Tools routes layers to external services, not downloads."}
  ]
}]
display_quiz(q8, max_width=1000)
```

## Question 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q9 = [{
  "question": "What is the key methodological point when using the Tools tab?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The selected textual layer (TEI / plain / spoken / stage directions) shapes the external results", "correct": True,
     "feedback": "Correct. Always record which layer you routed to the external tool."},
    {"answer": "Tools automatically normalises all spellings in the play", "correct": False,
     "feedback": "No. External tools will process whatever layer you provide."},
    {"answer": "Tools merges multiple plays into one dataset", "correct": False,
     "feedback": "No. Tools operates on the current play and selected layer."},
    {"answer": "Tools replaces the need for recording corpus and play ID", "correct": False,
     "feedback": "No. Reproducibility still requires corpus + play ID + tab/layer details."}
  ]
}]
display_quiz(q9, max_width=1000)
```

## Question 10 (short written task)

Pick any play in any corpus and write a reproducible “record note” with:
- corpus name
- play ID (slug)
- which tab you used
- one observation that can be verified

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from assessment import create_answer_box

create_answer_box(
    "record-note",
    rows=6,
    placeholder="Example: Corpus: … | Play ID: … | Tab: … | Observation: …",
)
```

````{admonition} Example answer (for self-check)
:class: tip, dropdown
Corpus: CalDraCor  
Play ID: calderon-vidaessueno  
Tab: Network  
Observation: The interface constructs edges by co-occurrence within segments; the summary panel reports the number of segments and basic network statistics (density, diameter, clustering), which can be documented alongside the selected play ID.
````
