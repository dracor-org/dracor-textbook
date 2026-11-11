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

# Self-Test: API

::::{admonition} Note
:class: note
This self-test helps you check your understanding of the chapter *API: Working with DraCor Programmatically*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, including when you answered correctly.
- The exercises at the end contain code that you can run and change. Launch this page as a notebook from the rocket icon at the top (see [Appendix A](../appendix/running-the-textbook-as-an-interactive-notebook.md)), or copy the code into your own Python environment.

Estimated time: 20–30 minutes.
::::

## Question 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [{
  "question": "In a REST API such as the DraCor API, what does the URL https://dracor.org/api/v1/corpora/gersh stand for?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "A resource: the German Shakespeare Drama Corpus, identified by its corpus name.", "correct": True,
     "feedback": "Correct. REST APIs are organised around resources, things with URLs, such as a corpus or a play."},
    {"answer": "A web page of the DraCor front-end that shows the corpus.", "correct": False,
     "feedback": "Not quite. The front-end URL would be https://dracor.org/gersh. The URL with /api/v1/ returns data (JSON), not a web page."},
    {"answer": "A function that has to be installed before it can be used.", "correct": False,
     "feedback": "No. An endpoint is a URL on the server; nothing needs to be installed to call it."},
    {"answer": "A database query written in XQuery.", "correct": False,
     "feedback": "No. DraCor uses XQuery internally, but the API hides this: we only send a request to a URL."}
  ]
}]
display_quiz(q1, max_width=1000)
```

## Question 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [{
  "question": "You have just requested the corpus gersh. To get one of its plays, you still have to give the corpus name again in the URL. Why?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Because REST interactions are stateless: each request is self-contained, and the server does not remember earlier requests.", "correct": True,
     "feedback": "Correct. This is one of the REST principles described in section 4.1."},
    {"answer": "Because the first request has expired after a few seconds.", "correct": False,
     "feedback": "No. Nothing expires; the server simply does not keep track of what you requested before."},
    {"answer": "Because play names are only unique across all of DraCor if combined with the API version.", "correct": False,
     "feedback": "No. The version (v1) is part of every URL, but it is the corpus name together with the play name that identifies a play."},
    {"answer": "Because the DraCor API does not follow REST.", "correct": False,
     "feedback": "No. The DraCor API follows REST, with a few pragmatic exceptions (see Question 5)."}
  ]
}]
display_quiz(q2, max_width=1000)
```

## Question 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [{
  "question": "In the front-end, you find a play at https://dracor.org/gersh/was-ihr-wollt. Which API URL returns its metadata?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "https://dracor.org/api/v1/corpora/gersh/plays/was-ihr-wollt", "correct": True,
     "feedback": "Correct. The front-end URL contains the corpus name and the play name in the same order as the API URL."},
    {"answer": "https://dracor.org/api/v1/plays/was-ihr-wollt", "correct": False,
     "feedback": "Not quite. A play is always addressed within its corpus: /corpora/{corpusname}/plays/{playname}."},
    {"answer": "https://dracor.org/api/v1/gersh/was-ihr-wollt", "correct": False,
     "feedback": "No. This mixes the front-end pattern with the API base path; the segments corpora and plays are missing."},
    {"answer": "https://dracor.org/gersh/was-ihr-wollt.json", "correct": False,
     "feedback": "No. The front-end does not serve data this way; data comes from URLs under /api/v1/."}
  ]
}]
display_quiz(q3, max_width=1000)
```

## Question 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [{
  "question": "Your code prints \"Request failed with status code: 404\". What should you check first?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Whether the corpus name and the play name in the URL are spelled correctly and exist.", "correct": True,
     "feedback": "Correct. 404 means \"not found\": the server works, but there is no resource at this URL. A typo in an identifier is the most common cause."},
    {"answer": "Whether you need an API key.", "correct": False,
     "feedback": "No. The DraCor API is open and needs no key; a missing key would not result in 404."},
    {"answer": "Whether the JSON response was parsed correctly.", "correct": False,
     "feedback": "No. With 404 there is no data to parse. Check the status code before working with the response."},
    {"answer": "Whether the request was successful; 404 is a variant of 200.", "correct": False,
     "feedback": "No. 200 means success; codes starting with 4 indicate a problem with the request."}
  ]
}]
display_quiz(q4, max_width=1000)
```

## Question 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [{
  "question": "How do you get the co-occurrence network of a play in different formats (CSV, GEXF, GraphML) from the DraCor API?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The format is part of the URL path, e.g. /networkdata/csv or /networkdata/gexf.", "correct": True,
     "feedback": "Correct. This is the \"pragmatic REST\" of the DraCor API: each format has its own URL, which makes it easy to link and share."},
    {"answer": "Only through the Accept header; the URL is always the same.", "correct": False,
     "feedback": "Not for the network data. The Accept header is used by two endpoints, /characters and /spoken-text-by-character; network formats are selected in the URL path."},
    {"answer": "By downloading JSON and converting it yourself.", "correct": False,
     "feedback": "Not necessary. The API offers these formats directly."},
    {"answer": "Only through the front-end, not through the API.", "correct": False,
     "feedback": "No. The download buttons of the front-end call exactly these API endpoints."}
  ]
}]
display_quiz(q5, max_width=1000)
```

## Question 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [{
  "question": "In https://dracor.org/api/v1/corpora/ger/plays/schiller-wilhelm-tell/spoken-text?sex=FEMALE, what is the role of sex=FEMALE?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It is a query parameter that filters the result: only text spoken by female characters.", "correct": True,
     "feedback": "Correct. Query parameters come after the ? and refine a request; the identifiers in the path select the resource."},
    {"answer": "It is a path parameter that selects a different play.", "correct": False,
     "feedback": "No. The play is selected by the path parameters (ger, schiller-wilhelm-tell); sex=FEMALE comes after the ?."},
    {"answer": "It changes the format of the response to CSV.", "correct": False,
     "feedback": "No. The format is unchanged (plain text); the parameter only filters the content."},
    {"answer": "It is ignored by the API.", "correct": False,
     "feedback": "No. Try both URLs in the browser and compare the results."}
  ]
}]
display_quiz(q6, max_width=1000)
```

## Question 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q7 = [{
  "question": "What is the difference between dracor.get_play(\"ger\", \"lessing-emilia-galotti\") in PyDraCor and requests.get(...) with the corresponding URL?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Both call the same API endpoint; PyDraCor builds the URL, sends the request and turns the JSON into Python objects for you.", "correct": True,
     "feedback": "Correct. PyDraCor is an API wrapper: shorter code, same API underneath."},
    {"answer": "PyDraCor reads the data from a local copy, requests from the server.", "correct": False,
     "feedback": "No. PyDraCor also sends requests to dracor.org (or to another DraCor instance you point it to)."},
    {"answer": "PyDraCor returns more data than the API provides.", "correct": False,
     "feedback": "No. A wrapper can only return what the API provides."},
    {"answer": "requests only works in the browser.", "correct": False,
     "feedback": "No. requests is a Python library; the browser is a separate way to send a request."}
  ]
}]
display_quiz(q7, max_width=1000)
```

## Exercise 1: From front-end URL to metadata

The following code turns a front-end URL into an API URL and prints some metadata of the play. Run it. Then find another play in the [German Shakespeare Drama Corpus](https://dracor.org/gersh) in the front-end, paste its URL and run the cell again.

```{code-cell} ipython3
import requests

frontend_url = "https://dracor.org/gersh/was-ihr-wollt"

corpusname, playname = frontend_url.replace("https://dracor.org/", "").split("/")
api_url = f"https://dracor.org/api/v1/corpora/{corpusname}/plays/{playname}"

response = requests.get(api_url, timeout=60)
if response.status_code == 200:
    play = response.json()
    print(play["title"], play["yearNormalized"], len(play["characters"]), "characters")
else:
    print(f"Request failed with status code: {response.status_code}")
```

Now change one letter in the play name and run the cell again. Which status code do you get, and why?

## Exercise 2: Corpus metadata as a table

The following code loads the metadata of all plays in the German Shakespeare Drama Corpus as a table. Run it, then answer with one or two lines of code: **Which play has the most words (`wordCountText`)?**

```{code-cell} ipython3
import io
import pandas as pd
import requests

url = "https://dracor.org/api/v1/corpora/gersh/metadata"
response = requests.get(url, headers={"Accept": "text/csv"}, timeout=60)
metadata_df = pd.read_csv(io.StringIO(response.text))

print(len(metadata_df), "plays")
metadata_df[["title", "yearNormalized", "numOfSpeakers", "wordCountText"]].head()
```

:::{dropdown} Solution
```python
metadata_df.sort_values(by="wordCountText", ascending=False)[["title", "wordCountText"]].head(1)
```
:::

## Exercise 3: The same play with PyDraCor

Get the play from Exercise 1 with PyDraCor and print the number of its characters. Do you get the same number as with `requests`?

```{code-cell} ipython3
from pydracor import DraCorAPI

dracor = DraCorAPI()
play = dracor.get_play("gersh", "was-ihr-wollt")
print(play.title)
```

:::{dropdown} Solution
```python
print(len(play.characters), "characters")
```
Both numbers are the same: PyDraCor calls the same API endpoint as the `requests` code in Exercise 1.
:::
