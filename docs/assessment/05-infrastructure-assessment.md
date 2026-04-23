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

::::{admonition} Note
:class: note
This self-test helps you check your understanding of the chapter *Infrastructure*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- If you are unsure, return to the relevant section of the chapter and verify the answer.

Estimated time: 10-15 minutes.
::::

## Question 1

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "According to the chapter, why does understanding DraCor's infrastructure matter for research?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "Because it allows researchers to avoid using the API entirely.", "correct": False, "feedback": "Not quite. The chapter does not argue against the API. Instead, it explains why understanding the system behind the API improves trust, adaptation, and critical awareness."},
      {"answer": "Because it helps build trust, enables adaptation, and fosters critical awareness of how data and metrics are produced.", "correct": True, "feedback": "Correct. These are the three main reasons given in the overview section."},
      {"answer": "Because only developers are allowed to use DraCor responsibly.", "correct": False, "feedback": "No. The chapter is written for learners and researchers, not only developers."},
      {"answer": "Because infrastructure mainly concerns server hardware, which humanists usually need to administer.", "correct": False, "feedback": "No. The chapter presents infrastructure more broadly as a socio-technical system, not only as hardware administration."}
    ]
  }
], max_width=1000)
:::

## Question 2

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "How does the chapter characterise DraCor from a technical perspective?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "As a single monolithic web application with one database and no external services.", "correct": False, "feedback": "No. The chapter explicitly says DraCor is not a single application."},
      {"answer": "As a system of interconnected services maintained by a community and embedded in a broader infrastructure landscape.", "correct": True, "feedback": "Correct. This formulation captures the chapter's central definition of DraCor as infrastructure."},
      {"answer": "As a front-end visualisation tool that only displays data generated elsewhere.", "correct": False, "feedback": "Too narrow. The front-end is only one component of the overall system."},
      {"answer": "As a local desktop program used mainly for TEI editing.", "correct": False, "feedback": "No. DraCor is not described as a desktop TEI editor."}
    ]
  }
], max_width=1000)
:::

## Question 3

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "Why does the chapter discuss DraCor's missing full-text search as an infrastructural example?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "Because the lack of search proves that DraCor is technically outdated and should be abandoned.", "correct": False, "feedback": "No. The chapter does not frame this as a reason to abandon DraCor."},
      {"answer": "Because it shows that infrastructure reflects architectural choices shaped by specific research priorities, especially structural and network analysis.", "correct": True, "feedback": "Correct. The example illustrates how DraCor's design grew out of particular research questions and priorities."},
      {"answer": "Because full-text search is impossible in XML databases such as eXist-db.", "correct": False, "feedback": "No. The chapter does not claim that XML databases cannot support search."},
      {"answer": "Because search is available only in local DraCor instances, not at dracor.org.", "correct": False, "feedback": "Incorrect. The point is that search was not built into the core design described in the chapter."}
    ]
  }
], max_width=1000)
:::

## Question 4

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "Which statement best matches the chapter's explanation of tactical infrastructure?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "It is a centralised platform imposed from above and designed before researchers define their needs.", "correct": False, "feedback": "No. That is the opposite of the tactical approach described in the chapter."},
      {"answer": "It is an infrastructure that grows bottom-up from concrete research needs, tools, practices, people, and code.", "correct": True, "feedback": "Correct. This summarises the chapter's discussion of tactical infrastructure and its relevance for DraCor and CLS INFRA."},
      {"answer": "It is a military metaphor used to describe secure server management.", "correct": False, "feedback": "No. The term is used conceptually, not in a military or security sense."},
      {"answer": "It refers only to temporary prototypes that should never become sustainable infrastructures.", "correct": False, "feedback": "Not quite. The chapter uses the term to describe a bottom-up ecosystem, not merely a temporary prototype."}
    ]
  }
], max_width=1000)
:::

## Question 5

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "What is the role of eXist-db in the DraCor system, according to the chapter?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "It is the core XML database in which the DraCor API is implemented as an eXist-db application written in XQuery.", "correct": True, "feedback": "Correct. The chapter identifies eXist-db as the core database and explains that the API logic is implemented there in XQuery."},
      {"answer": "It is a graphical front-end for editing TEI documents in the browser.", "correct": False, "feedback": "No. That is not how eXist-db is described in the chapter."},
      {"answer": "It is the Python service that calculates network metrics.", "correct": False, "feedback": "No. That role belongs to the separate Metrics Service."},
      {"answer": "It is the RDF triple store used for SPARQL queries.", "correct": False, "feedback": "Incorrect. The triple store is a separate component."}
    ]
  }
], max_width=1000)
:::

## Question 6

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "Why does the chapter describe the Metrics Service as an example of a microservice architecture?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "Because it stores all TEI files in a separate GitHub repository.", "correct": False, "feedback": "No. GitHub repositories are discussed elsewhere, but that is not what makes the Metrics Service a microservice."},
      {"answer": "Because it is a specialised external service that calculates network metrics and communicates with the rest of the system via APIs.", "correct": True, "feedback": "Correct. The chapter uses this component to illustrate how specialised services can handle specific tasks within a larger system."},
      {"answer": "Because it replaces the front-end whenever the React application is unavailable.", "correct": False, "feedback": "No. The Metrics Service does not replace the front-end."},
      {"answer": "Because it runs inside the user's browser as part of the single-page application.", "correct": False, "feedback": "Incorrect. The service is separate from the browser-based front-end."}
    ]
  }
], max_width=1000)
:::

## Question 7

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "What is one of the chapter's main reasons for running DraCor locally with Docker?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "It is the only way to use the DraCor API at all.", "correct": False, "feedback": "No. Earlier chapters already use the public API at dracor.org."},
      {"answer": "It allows researchers to work with a controlled version of the data and software, which supports reproducibility.", "correct": True, "feedback": "Correct. The chapter emphasises version control, independence from the production server, and reproducibility."},
      {"answer": "It automatically adds full-text search to all corpora.", "correct": False, "feedback": "No. The chapter does not present local deployment as a solution to that feature gap."},
      {"answer": "It removes the need for TEI-encoded source texts.", "correct": False, "feedback": "Incorrect. Local DraCor still depends on DraCor-compatible TEI data."}
    ]
  }
], max_width=1000)
:::

## Question 8

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "According to the chapter, what is the difference between a Docker image and a Docker container?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "An image is a running service, whereas a container is the static file stored on DockerHub.", "correct": False, "feedback": "No. This reverses the distinction."},
      {"answer": "An image is a read-only template or snapshot, whereas a container is a running instance created from that image.", "correct": True, "feedback": "Correct. This is the basic distinction explained in the Docker section."},
      {"answer": "An image is used only for databases, whereas a container is used only for front-end applications.", "correct": False, "feedback": "No. The distinction is not based on application type."},
      {"answer": "There is no practical difference; the chapter uses the two words interchangeably.", "correct": False, "feedback": "Incorrect. The chapter clearly distinguishes between them."}
    ]
  }
], max_width=1000)
:::

## Question 9

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "What is the correct order for loading a corpus into a local DraCor instance, as described in the hands-on section?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "First calculate network metrics manually, then upload the front-end, then create a GitHub issue.", "correct": False, "feedback": "No. That is not the workflow described in the chapter."},
      {"answer": "First register the corpus by posting its metadata, then trigger loading of the actual play data.", "correct": True, "feedback": "Correct. The chapter explicitly presents corpus loading as a two-step process: register, then load."},
      {"answer": "First open the front-end in the browser, then drag and drop TEI files, then restart Docker.", "correct": False, "feedback": "No. The chapter describes loading through admin API endpoints, not drag-and-drop through the interface."},
      {"answer": "First send JSON metadata to the Metrics Service, then export RDF to the triple store.", "correct": False, "feedback": "Incorrect. That does not match the described workflow."}
    ]
  }
], max_width=1000)
:::

## Question 10

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

display_quiz([
  {
    "question": "How does the chapter describe the front-end in relation to the API?",
    "type": "multiple_choice",
    "answers": [
      {"answer": "As an independent data source that does not rely on the API once the page has loaded.", "correct": False, "feedback": "No. The chapter stresses that the front-end communicates with the API throughout its operations."},
      {"answer": "As an API client: a React single-page application that sends requests to the DraCor API and displays the results.", "correct": True, "feedback": "Correct. This directly matches the chapter's description of the front-end."},
      {"answer": "As a replacement for the API, used only when the XML database is offline.", "correct": False, "feedback": "Incorrect. The front-end depends on the API rather than replacing it."},
      {"answer": "As a command-line tool that wraps curl requests for beginners.", "correct": False, "feedback": "No. The front-end is a web application, not a command-line tool."}
    ]
  }
], max_width=1000)
:::
