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

# Self-test: Infrastructure

````{admonition} Note
:class: note
This self-test helps you check your understanding of *Infrastructure*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- If you are unsure, return to the relevant section and verify the answer.

Estimated time: 10–15 minutes.
````

## Question 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [{
  "question": "Why does understanding DraCor's infrastructure matter for research?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because it allows researchers to avoid using the API entirely.", "correct": False,
     "feedback": "Not quite. The point is not to avoid the API, but to understand the system behind it and gain trust, adaptability, and critical awareness."},
    {"answer": "Because it helps build trust, enables adaptation, and fosters critical awareness of how data and metrics are produced.", "correct": True,
     "feedback": "Correct. These are the three main reasons given in the overview section."},
    {"answer": "Because only developers are allowed to use DraCor responsibly.", "correct": False,
     "feedback": "No. This material is aimed at learners and researchers, not only developers."},
    {"answer": "Because infrastructure mainly concerns server hardware, which humanists usually need to administer.", "correct": False,
     "feedback": "No. Infrastructure is presented here as a socio-technical system, not just hardware administration."}
  ]
}]
display_quiz(q1, max_width=1000)
```

## Question 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [{
  "question": "How is DraCor characterised here from a technical perspective?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "As a single monolithic web application with one database and no external services.", "correct": False,
     "feedback": "No. DraCor is presented as more than a single application."},
    {"answer": "As a system of interconnected services maintained by a community and embedded in a broader infrastructure landscape.", "correct": True,
     "feedback": "Correct. This captures the core definition of DraCor as infrastructure."},
    {"answer": "As a front-end visualisation tool that only displays data generated elsewhere.", "correct": False,
     "feedback": "Too narrow. The front-end is only one component of the overall system."},
    {"answer": "As a local desktop program used mainly for TEI editing.", "correct": False,
     "feedback": "No. DraCor is not described as a desktop TEI editor."}
  ]
}]
display_quiz(q2, max_width=1000)
```

## Question 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [{
  "question": "Why is DraCor's missing full-text search discussed as an infrastructural example?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because the lack of search proves that DraCor is technically outdated and should be abandoned.", "correct": False,
     "feedback": "No. This is not presented as a reason to abandon DraCor."},
    {"answer": "Because it shows that infrastructure reflects architectural choices shaped by specific research priorities, especially structural and network analysis.", "correct": True,
     "feedback": "Correct. The example illustrates how DraCor's design grew out of particular research questions and priorities."},
    {"answer": "Because full-text search is impossible in XML databases such as eXist-db.", "correct": False,
     "feedback": "No. There is no claim that XML databases cannot support search."},
    {"answer": "Because search is available only in local DraCor instances, not at dracor.org.", "correct": False,
     "feedback": "Incorrect. The point is that search was not built into the core design being discussed."}
  ]
}]
display_quiz(q3, max_width=1000)
```

## Question 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [{
  "question": "Which statement best matches the explanation of tactical infrastructure?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It is a centralised platform imposed from above and designed before researchers define their needs.", "correct": False,
     "feedback": "No. That is the opposite of the tactical approach described here."},
    {"answer": "It is an infrastructure that grows bottom-up from concrete research needs, tools, practices, people, and code.", "correct": True,
     "feedback": "Correct. This summarises tactical infrastructure and its relevance for DraCor and CLS INFRA."},
    {"answer": "It is a military metaphor used to describe secure server management.", "correct": False,
     "feedback": "No. The term is used conceptually, not in a military or security sense."},
    {"answer": "It refers only to temporary prototypes that should never become sustainable infrastructures.", "correct": False,
     "feedback": "Not quite. The term is used for a bottom-up ecosystem, not merely a temporary prototype."}
  ]
}]
display_quiz(q4, max_width=1000)
```

## Question 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [{
  "question": "What is the role of eXist-db in the DraCor system?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It is the core XML database in which the DraCor API is implemented as an eXist-db application written in XQuery.", "correct": True,
     "feedback": "Correct. eXist-db is the core database, and the API logic is implemented there in XQuery."},
    {"answer": "It is a graphical front-end for editing TEI documents in the browser.", "correct": False,
     "feedback": "No. That is not how eXist-db is described here."},
    {"answer": "It is the Python service that calculates network metrics.", "correct": False,
     "feedback": "No. That role belongs to the separate Metrics Service."},
    {"answer": "It is the RDF triple store used for SPARQL queries.", "correct": False,
     "feedback": "Incorrect. The triple store is a separate component."}
  ]
}]
display_quiz(q5, max_width=1000)
```

## Question 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [{
  "question": "Why is the Metrics Service presented as an example of a microservice architecture?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because it stores all TEI files in a separate GitHub repository.", "correct": False,
     "feedback": "No. GitHub repositories are discussed elsewhere, but that is not what makes the Metrics Service a microservice."},
    {"answer": "Because it is a specialised external service that calculates network metrics and communicates with the rest of the system via APIs.", "correct": True,
     "feedback": "Correct. This component illustrates how specialised services can handle specific tasks within a larger system."},
    {"answer": "Because it replaces the front-end whenever the React application is unavailable.", "correct": False,
     "feedback": "No. The Metrics Service does not replace the front-end."},
    {"answer": "Because it runs inside the user's browser as part of the single-page application.", "correct": False,
     "feedback": "Incorrect. The service is separate from the browser-based front-end."}
  ]
}]
display_quiz(q6, max_width=1000)
```

## Question 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [{
  "question": "What is one major reason for running DraCor locally with Docker?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It is the only way to use the DraCor API at all.", "correct": False,
     "feedback": "No. The public API at dracor.org can already be used without a local setup."},
    {"answer": "It allows researchers to work with a controlled version of the data and software, which supports reproducibility.", "correct": True,
     "feedback": "Correct. The key advantages include version control, independence from the production server, and reproducibility."},
    {"answer": "It automatically adds full-text search to all corpora.", "correct": False,
     "feedback": "No. Local deployment is not presented as a solution to that feature gap."},
    {"answer": "It removes the need for TEI-encoded source texts.", "correct": False,
     "feedback": "Incorrect. Local DraCor still depends on DraCor-compatible TEI data."}
  ]
}]
display_quiz(q7, max_width=1000)
```

## Question 8

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q8 = [{
  "question": "What is the difference between a Docker image and a Docker container?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "An image is a running service, whereas a container is the static file stored on DockerHub.", "correct": False,
     "feedback": "No. This reverses the distinction."},
    {"answer": "An image is a read-only template or snapshot, whereas a container is a running instance created from that image.", "correct": True,
     "feedback": "Correct. This is the basic distinction explained in the Docker section."},
    {"answer": "An image is used only for databases, whereas a container is used only for front-end applications.", "correct": False,
     "feedback": "No. The distinction is not based on application type."},
    {"answer": "There is no practical difference; the two words are used interchangeably.", "correct": False,
     "feedback": "Incorrect. The distinction is made quite clearly."}
  ]
}]
display_quiz(q8, max_width=1000)
```

## Question 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q9 = [{
  "question": "What is the correct order for loading a corpus into a local DraCor instance, as described in the hands-on section?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "First calculate network metrics manually, then upload the front-end, then create a GitHub issue.", "correct": False,
     "feedback": "No. That is not the workflow described here."},
    {"answer": "First register the corpus by posting its metadata, then trigger loading of the actual play data.", "correct": True,
     "feedback": "Correct. Corpus loading is presented as a two-step process: register, then load."},
    {"answer": "First open the front-end in the browser, then drag and drop TEI files, then restart Docker.", "correct": False,
     "feedback": "No. Loading is described through admin API endpoints, not drag-and-drop through the interface."},
    {"answer": "First send JSON metadata to the Metrics Service, then export RDF to the triple store.", "correct": False,
     "feedback": "Incorrect. That does not match the described workflow."}
  ]
}]
display_quiz(q9, max_width=1000)
```

## Question 10

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q10 = [{
  "question": "How is the front-end described in relation to the API?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "As an independent data source that does not rely on the API once the page has loaded.", "correct": False,
     "feedback": "No. The front-end communicates with the API throughout its operations."},
    {"answer": "As an API client: a React single-page application that sends requests to the DraCor API and displays the results.", "correct": True,
     "feedback": "Correct. This directly matches the description of the front-end."},
    {"answer": "As a replacement for the API, used only when the XML database is offline.", "correct": False,
     "feedback": "Incorrect. The front-end depends on the API rather than replacing it."},
    {"answer": "As a command-line tool that wraps curl requests for beginners.", "correct": False,
     "feedback": "No. The front-end is a web application, not a command-line tool."}
  ]
}]
display_quiz(q10, max_width=1000)
```
