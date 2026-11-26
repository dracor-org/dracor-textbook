# Contributing to the DraCor Textbook

The [DraCor Textbook](https://textbook.dracor.org) is an Open Educational Resource (OER) for working with the Programmable Corpora of [DraCor](https://dracor.org). It is under active development, and your feedback helps us improve it. Its editorial guidelines and decisions are documented in the [wiki](https://github.com/dracor-org/dracor-textbook/wiki).

## Questions and feedback

Please open an issue in this repository using one of the two templates:

- [**Ask a question**](https://github.com/dracor-org/dracor-textbook/issues/new?labels=question&template=question.yml) about the content, methods, code and notebooks, or the build of the book. Tell us which page your question is about and what you have tried so far.
- [**Give feedback**](https://github.com/dracor-org/dracor-textbook/issues/new?labels=feedback&template=feedback.yml) to suggest an improvement, for example clearer wording, an additional example, a correction of an error or a broken link, or a better exercise or reference. Tell us which page your feedback is about, what is there now and what you suggest. You can also say whether you would like to open a pull request yourself.

We are particularly interested in hearing from you if you use the textbook in teaching: which chapters you used, in what kind of course, and what worked well or did not.

For other ways to reach the DraCor community, see [Get in Touch](https://dracor.org/doc/get-in-touch) on dracor.org.

## Suggesting changes

Changes to the `main` branch are made through pull requests:

- Every pull request is built automatically with Jupyter Book (see `.github/workflows/ci-book.yml`).
- A pull request needs the approving review of a code owner before it can be merged. The code owners are listed in [`.github/CODEOWNERS`](.github/CODEOWNERS).
- To build the book on your own computer, follow the instructions under “Build Locally” in the [README](README.md).

Opening an issue or a pull request does not in itself make you an author of a chapter (see [Editorial Review and Release Tracking](https://github.com/dracor-org/dracor-textbook/wiki/Editorial-Review-and-Release-Tracking)).

## Writing and editing chapters

The conventions for language, terminology, citations, footnotes, cross-references, filenames and figures are collected in the [Guidelines for Authors and Editors](https://github.com/dracor-org/dracor-textbook/wiki/Guidelines-for-Authors-and-Editors) on the wiki. The textbook is written in British English, and references are cited from the shared `docs/references.bib`.

The chapters follow the chapter template described in the [Main Documentation](https://github.com/dracor-org/dracor-textbook/wiki/DraCor-Textbook-Wiki) of the wiki. Before the References, chapters following the template have two sections:

- **AI Use Declaration**: whether and how AI tools were used for the chapter. The use of AI tools has to be declared, also for contributions to an existing chapter.
- **Author Contributions**: contributor roles according to the [CRediT](https://credit.niso.org/) taxonomy.

For the use of material from other sources and its attribution, see the [OER Guidelines](https://github.com/dracor-org/dracor-textbook/wiki/Open-Educational-Resource-(OER)-Guidelines).

## Licence and citation

The DraCor Textbook is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). How to cite the textbook or a single chapter is described under “Suggested Citation” in the [README](README.md) and in [`CITATION.cff`](CITATION.cff).
