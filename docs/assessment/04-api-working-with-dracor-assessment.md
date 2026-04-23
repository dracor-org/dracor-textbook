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

# Self-test: API

````{admonition} Note
:class: note
This self-test supports Chapter 4 (*API: Working with DraCor Programmatically*). It checks key concepts and basic hands-on skills.

- There is no grading and nothing is stored.
- Multiple-choice questions provide feedback for every option.
- Coding tasks are presented as (a) a student prompt, (b) a reference solution shown as code, and (c) an executed reference output.

Estimated time: 25–40 minutes.
````

## Question 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [{
  "question": "In the DraCor context, what does the API primarily do?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "It is the documentation website at https://dracor.org/doc/api", "correct": False,
     "feedback": "Not quite. That is the Swagger UI documentation *about* the API."},
    {"answer": "It is the programmatic interface that returns data (e.g. JSON, CSV, TEI/XML) at https://dracor.org/api/v1/", "correct": True,
     "feedback": "Correct. The API is the data/service interface, and the front-end is one client of it."},
    {"answer": "It is only used for downloading GEXF files for Gephi", "correct": False,
     "feedback": "No. Downloads are only one part. The API provides corpora, plays, text layers, characters, networks, and more."},
    {"answer": "It is a local file repository of TEI documents", "correct": False,
     "feedback": "No. TEI exists as a source layer, but the API is a web service that returns processed data from the backend."}
  ]
}]
display_quiz(q1, max_width=1000)
```

## Question 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [{
  "question": "What is the most accurate statement about Swagger UI for DraCor?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Swagger UI is the API itself", "correct": False,
     "feedback": "No. Swagger UI is documentation and a testing interface, not the API."},
    {"answer": "Swagger UI renders the OpenAPI specification as interactive documentation and lets you try requests", "correct": True,
     "feedback": "Correct. It is a human-friendly interface to the OpenAPI contract."},
    {"answer": "Swagger UI requires authentication for all endpoints", "correct": False,
     "feedback": "No. Public endpoints can be used without authentication."},
    {"answer": "Swagger UI returns TEI/XML only", "correct": False,
     "feedback": "No. Swagger UI shows endpoints that return JSON, CSV, XML, and plain text (depending on endpoint)."}
  ]
}]
display_quiz(q2, max_width=1000)
```

## Question 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [{
  "question": "Which option correctly distinguishes path parameters and query parameters?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Path parameters come after '?' and query parameters are inside the URL path", "correct": False,
     "feedback": "No. That is inverted."},
    {"answer": "Path parameters are required parts of the URL (e.g. /corpora/{corpusname}); query parameters are optional key–value pairs after '?' (e.g. ?include=metrics)", "correct": True,
     "feedback": "Correct. In DraCor, both types are used."},
    {"answer": "Both are always optional in DraCor", "correct": False,
     "feedback": "No. Path parameters are typically required for play-level endpoints."},
    {"answer": "Query parameters are used only for file formats (CSV/GEXF)", "correct": False,
     "feedback": "No. DraCor often encodes formats in the path (e.g. /networkdata/gexf), but query parameters are also used for filters (e.g. sex=FEMALE)."}
  ]
}]
display_quiz(q3, max_width=1000)
```

## Question 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [{
  "question": "You request https://dracor.org/api/v1/corpora/rus/plays/hamlet and receive status code 404. What is the most likely explanation?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "The API server is down (server-side error)", "correct": False,
     "feedback": "A server outage is more likely to yield 5xx codes. 404 usually indicates a missing resource."},
    {"answer": "Your request is wrong because the play identifier does not exist in that corpus (client-side mismatch)", "correct": True,
     "feedback": "Correct. Identifiers are scoped: a play slug must belong to the specified corpus."},
    {"answer": "You forgot to add an Accept header", "correct": False,
     "feedback": "Missing Accept headers do not typically cause 404; they affect formats when the endpoint supports negotiation."},
    {"answer": "DraCor blocks programmatic access without authentication", "correct": False,
     "feedback": "No. Public endpoints are designed for unauthenticated GET requests."}
  ]
}]
display_quiz(q4, max_width=1000)
```

## Question 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [{
  "question": "How do you request the character list as CSV from an endpoint that supports content negotiation (rather than path suffixes)?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "Add ?format=csv to the URL", "correct": False,
     "feedback": "Not in this case. The chapter explains content negotiation via the Accept header."},
    {"answer": "Send an HTTP header Accept: text/csv", "correct": True,
     "feedback": "Correct. This is the standard mechanism for requesting a representation (format) where supported."},
    {"answer": "Replace /api/v1/ with /csv/", "correct": False,
     "feedback": "No. That is not a DraCor convention."},
    {"answer": "CSV is not available via the API", "correct": False,
     "feedback": "CSV is available for specific endpoints (e.g. characters, spoken-text-by-character, metadata) via path or negotiation."}
  ]
}]
display_quiz(q5, max_width=1000)
```

## Question 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q6 = [{
  "question": "Which three-step identifier flow is correct when navigating the DraCor API?",
  "type": "multiple_choice",
  "answers": [
    {"answer": "/plays → /corpora/{corpusname} → /corpora/{corpusname}/plays/{playname}", "correct": False,
     "feedback": "No. DraCor is organised around corpora first."},
    {"answer": "/corpora → /corpora/{corpusname} → /corpora/{corpusname}/plays/{playname}", "correct": True,
     "feedback": "Correct. Outputs of one request provide identifiers for the next."},
    {"answer": "/info → /tei → /characters", "correct": False,
     "feedback": "No. Those are endpoints, but not the identifier cascade."},
    {"answer": "/metrics → /networkdata → /corpora", "correct": False,
     "feedback": "No. This inverts the typical navigation pattern."}
  ]
}]
display_quiz(q6, max_width=1000)
```

## Question 7

Student exercise (copy into a notebook, fill in, run):

```python
import requests

url = "https://dracor.org/api/v1/corpora"
params = {"include": "metrics"}

# TODO: send request with a timeout
# TODO: check status code (raise_for_status is fine)
# TODO: parse JSON to a Python list
# TODO: print the number of corpora
# TODO: print the first 5 corpus identifiers and titles: "<name>: <title>"
```

Self-check:
- You should see an integer number of corpora.
- You should see 5 lines like `ger: German Drama Corpus` (exact titles vary).

````{admonition} Reference solution (code)
:class: tip, dropdown
```python
import requests

url = "https://dracor.org/api/v1/corpora"
params = {"include": "metrics"}

r = requests.get(url, params=params, timeout=30)
if r.status_code != 200:
    print(f"Request failed with status code: {r.status_code}")
else:
    corpora = r.json()
    print(f"Number of corpora: {len(corpora)}")
    for c in corpora[:5]:
        print(f"{c.get('name')}: {c.get('title')}")
```
````

Executed reference output:

```{code-cell} ipython3
:tags: [remove-input]
import requests

url = "https://dracor.org/api/v1/corpora"
params = {"include": "metrics"}

try:
    r = requests.get(url, params=params, timeout=30)
    if r.status_code != 200:
        print(f"Request failed with status code: {r.status_code}")
    else:
        corpora = r.json()
        print(f"Number of corpora: {len(corpora)}")
        for c in corpora[:5]:
            print(f"{c.get('name')}: {c.get('title')}")
except Exception as e:
    print(f"Request failed with error: {e}")
```

## Question 8

Student exercise (copy into a notebook, fill in, run):

```python
import requests

API_URL = "https://dracor.org/api/v1/"
corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"{API_URL}corpora/{corpusname}/plays/{playname}"

# TODO: send a GET request with a timeout
# TODO: if status 200, parse the JSON response
# TODO: print:
#   - the play title
#   - the normalised year
#   - the number of speakers
#   - the average degree (if available)
# TODO: otherwise, print "Request failed with status code: <status>"
```

Self-check:
- You should see basic play metadata for *Emilia Galotti*.
- The output should contain the title, a year, and at least one network-related value.

````{admonition} Reference solution (code)
:class: tip, dropdown
```python
import requests

API_URL = "https://dracor.org/api/v1/"
corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"{API_URL}corpora/{corpusname}/plays/{playname}"

r = requests.get(url, timeout=15)

if r.status_code != 200:
    print(f"Request failed with status code: {r.status_code}")
else:
    data = r.json()
    print(f"Title: {data.get('title')}")
    print(f"Year: {data.get('yearNormalized')}")
    print(f"Speakers: {data.get('numOfSpeakers')}")
    print(f"Average degree: {data.get('averageDegree')}")
```
````

Executed reference output:

```{code-cell} ipython3
:tags: [remove-input]
import requests

API_URL = "https://dracor.org/api/v1/"
corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"{API_URL}corpora/{corpusname}/plays/{playname}"

try:
    r = requests.get(url, timeout=15)
    if r.status_code != 200:
        print(f"Request failed with status code: {r.status_code}")
    else:
        data = r.json()
        print(f"Title: {data.get('title')}")
        print(f"Year: {data.get('yearNormalized')}")
        print(f"Speakers: {data.get('numOfSpeakers')}")
        print(f"Average degree: {data.get('averageDegree')}")
except Exception as e:
    print(f"Request failed with error: {e}")
```

## Question 9

Student exercise (copy into a notebook, run). The endpoint is intentionally wrong:

```python
import requests

url = "https://dracor.org/api/v1/corpora/rus/plays/lessing-emilia-galotti"
r = requests.get(url, timeout=15)

# TODO: if status 200, print the play title from JSON
# TODO: otherwise, print "Request failed with status code: <status>"
```

Self-check:
- You should get a non-200 status code, typically 404.
- This shows that a play slug only works inside the correct corpus.

````{admonition} Reference solution (code)
:class: tip, dropdown
```python
import requests

url = "https://dracor.org/api/v1/corpora/rus/plays/lessing-emilia-galotti"
r = requests.get(url, timeout=15)

if r.status_code == 200:
    data = r.json()
    print(f"Play title: {data.get('title')}")
else:
    print(f"Request failed with status code: {r.status_code}")
```
````

Executed reference output:

```{code-cell} ipython3
:tags: [remove-input]
import requests

url = "https://dracor.org/api/v1/corpora/rus/plays/lessing-emilia-galotti"

try:
    r = requests.get(url, timeout=15)
    if r.status_code == 200:
        data = r.json()
        print(f"Play title: {data.get('title')}")
    else:
        print(f"Request failed with status code: {r.status_code}")
except Exception as e:
    print(f"Request failed with error: {e}")
```

## Question 10

Student exercise (copy into a notebook, fill in, run):

```python
import requests

corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"https://dracor.org/api/v1/corpora/{corpusname}/plays/{playname}/characters"

# TODO: request CSV using Accept: text/csv
# TODO: print the first 5 non-empty lines of the response
```

Self-check:
- You should see a header row (CSV column names), then character rows.

````{admonition} Reference solution (code)
:class: tip, dropdown
```python
import requests

corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"https://dracor.org/api/v1/corpora/{corpusname}/plays/{playname}/characters"

r = requests.get(url, headers={"Accept": "text/csv"}, timeout=15)

if r.status_code != 200:
    print(f"Request failed with status code: {r.status_code}")
else:
    lines = [ln for ln in r.text.splitlines() if ln.strip()]
    for ln in lines[:5]:
        print(ln)
```
````

Executed reference output:

```{code-cell} ipython3
:tags: [remove-input]
import requests

corpusname = "ger"
playname = "lessing-emilia-galotti"
url = f"https://dracor.org/api/v1/corpora/{corpusname}/plays/{playname}/characters"

try:
    r = requests.get(url, headers={"Accept": "text/csv"}, timeout=15)
    if r.status_code != 200:
        print(f"Request failed with status code: {r.status_code}")
    else:
        lines = [ln for ln in r.text.splitlines() if ln.strip()]
        for ln in lines[:5]:
            print(ln)
except Exception as e:
    print(f"Request failed with error: {e}")
```
