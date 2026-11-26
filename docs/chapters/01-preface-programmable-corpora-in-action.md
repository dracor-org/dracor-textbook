---
title: "Preface: Programmable Corpora in Action"
myst:
  substitutions:
   chap_title: "Preface"
authors: "Antonio Rojas Castro"
date: "2026-11-26"
description: "This preface introduces the DraCor Textbook as an Open Educational Resource (OER), explains the concept of Programmable Corpora, outlines its target audiences and learning scenarios and presents the main ways in which the Textbook can be used for self-study and lecturer-guided teaching."
keywords: ["DraCor Textbook", "Programmable Corpora", "Open Educational Resource", "active learning", "self-study", "Digital Humanities"]
license: "CC BY 4.0"
---

# Preface: Programmable Corpora in Action

```{admonition} Chapter metadata
:class: tip
**Author:** Antonio Rojas Castro  
**Version:** 0.7 (2026-11-26)  
**Review status:** reviewed  
**Reviewers:** Frank Fischer; Julia Jennifer Beine; Ingo Börner
```

## 1. About This Textbook

The **DraCor Textbook** is an Open Educational Resource (OER) developed as part of the DraCorOS project. It introduces [DraCor](https://dracor.org/), an open infrastructure for digital drama analysis, and shows how we can work with its Programmable Corpora {cite:p}`fischer2019programmable`. The chapters follow a learning sequence that combines conceptual explanations with practical tasks, exercises and guidance for teaching.[^notebooks]

## 2. DraCor and Programmable Corpora

A Programmable Corpus combines a collection of digital texts with documented interfaces through which texts, metadata and derived data can be retrieved and processed. In DraCor, openly available TEI/XML corpora are connected to an **A**pplication **P**rogramming **I**nterface (API) and a web front-end. This combination supports both direct exploration and reproducible computational research {cite:p}`borner2023cls,borner2025cls`. Both reports are also available in HTML ([D7.1](https://dracor-org.github.io/dracor-tech-reports/clsinfra-d71/), [D7.4](https://dracor-org.github.io/dracor-tech-reports/clsinfra-d74/)).

This preface introduces the purpose and scope of the Textbook. The five chapters that follow explain the individual components and workflows in greater detail, from corpus building and TEI encoding to the front-end, API-based access and local infrastructure.

[Chapter 5, API: Working with DraCor Programmatically](05-api-working-with-dracor-programmatically.md) is an executable Jupyter Notebook. [Appendix A, Running the Textbook as an Interactive Notebook](../appendix/running-the-textbook-as-an-interactive-notebook.md) explains how to open it in your browser and run the code.

## 3. Who Is the Textbook For?

The Textbook is intended for advanced BA and MA students, including humanities students with little or no background in Digital Humanities. Researchers and independent learners can use it for self-study. Lecturers and trainers can adapt individual chapters for a seminar or workshop. These audiences are also described in our DHd 2027 abstract, *Das DraCor Textbook: Programmable Corpora Lehren und Lernen* (forthcoming).

```{figure} ../images/preface/target-audience.png
:alt: Diagram showing the audiences for the DraCor Textbook, including BA and MA students, researchers, independent learners, lecturers and trainers.
:width: 90%

The DraCor Textbook supports self-study and classroom teaching, including courses for advanced BA and MA students.
```

No previous programming experience is required. Chapters introduce technical concepts gradually and state their specific requirements at the beginning. Readers may follow the Textbook sequentially or select individual chapters according to their learning or teaching context.

## 4. How to Use This Textbook?

The DraCor Textbook supports two main learning scenarios: independent self-study and guided teaching or training. In both cases, it encourages active learning. Learners are not expected only to read about methods and tools. They are also invited to inspect data, navigate interfaces, encode texts, make API requests, compare results and reflect on the assumptions and limitations of each workflow.

### Self-Study

Learners working independently may follow the DraCor Textbook in sequence or begin with a chapter related to a specific interest. At the beginning of each chapter, the requirements and learning outcomes indicate what prior knowledge is expected and what learners should be able to understand or do after completing it.

The theoretical background introduces the main concepts, while the practical examples show how they are applied. Learners should reproduce these examples where possible and complete the exercises before proceeding to the self-test.

The self-tests are intended for formative feedback rather than grading. Answers are not stored, and the feedback explains why an option is correct or incorrect. When an answer is unclear, learners are encouraged to return to the relevant chapter section, interface or tool and verify the result. The Glossary, Further Reading and Resources and Next Steps sections provide additional support for reviewing concepts or continuing with related topics.

### Classroom Teaching and Training

Lecturers and trainers may use the Textbook as the basis for an introductory course on building and analysing digital drama corpora with DraCor or select individual chapters and activities for shorter teaching units. The sequence, pace and level of technical detail can be adapted to the participants’ previous experience and the available teaching time.

The Teaching Notes at the end of each chapter suggest session formats and group activities. These may include guided demonstrations, individual or paired exercises, comparisons between plays or corpora and collective reflection on modelling choices. The practical examples may first be presented by the lecturer and then repeated or adapted by learners. Self-tests may be completed individually during or after a session and used to identify aspects that require further explanation.

In this scenario, the lecturer does not only demonstrate procedures but also supports learners in formulating questions, documenting their decisions and distinguishing between what the data or interface shows and how these observations may be interpreted.

## 5. What Can We Do with DraCor?

The following examples show what you can do with DraCor as you work through the chapters:

- [Chapter 2](02-corpus-building-in-dracor.md) covers **building a drama corpus:** collecting, preparing and adapting dramatic texts for a reusable and openly maintained corpus;
- [Chapter 3](03-tei-encoding-preparing-texts-for-programmable-corpora.md) covers **preparing texts in TEI/XML:** encoding the structure and features of dramatic texts according to the DraCor schema, using manual and semi-automatic workflows;
- [Chapter 4](04-front-end-navigating-dracor.md) covers **exploring corpora and plays through the front-end:** navigating corpus overviews and pages of individual plays, interpreting network visualisations and speech-distribution views, contextualising observations in the full-text view and retrieving available data layers;
- [Chapter 5](05-api-working-with-dracor-programmatically.md) covers **working with DraCor programmatically:** using the interactive API documentation and Python to retrieve texts, metadata, character information and derived metrics, and to extend analysis from individual plays to complete corpora;
- [Chapter 6](06-dracor-in-the-context-of-research-infrastructures.md) covers **working with DraCor as a research infrastructure:** understanding how its components interact and using Docker to run a local instance for custom corpora, controlled data versions and reproducible research.

Together, these use cases guide learners from the preparation of structured textual data to its exploration, programmatic analysis and reproducible deployment. Each chapter also identifies the modelling choices, data dependencies and technical limitations relevant to its workflow.

## 6. The Textbook as a Living Resource

We welcome suggestions for corrections, examples and teaching activities. Readers can [open an issue on GitHub](https://github.com/dracor-org/dracor-textbook/issues/new/choose) or share their experiences of teaching and learning with DraCor through the [DraCor Blog](https://dracor.hypotheses.org/).

## 7. Use of AI in the DraCor Textbook

Each chapter includes an AI Use Declaration. As an editor, Antonio Rojas Castro used ChatGPT (OpenAI) to review wording and organise feedback across the Textbook.

The editorial team used Claude Code (Anthropic, Claude Opus 5.5) for the following tasks.

- configuring Jupyter Book, bibliography formatting, the EPUB edition and its cover, and the workflow for attaching the EPUB to releases
- building the Textbook, checking links, testing code examples against the DraCor API and checking statements against the DraCor documentation
- checking bibliography entries, DOIs and software metadata
- transcribing handwritten review notes and drafting GitHub issues, comments and pull request descriptions, labelled “Drafted with Claude Opus 5.5” or “Generated with Claude Code”
- preparing citation metadata, the licence file and repository contribution guidelines

A member of the editorial team reviewed and approved each change before merging it. The authors and editors take responsibility for the content.

## 8. Author Contributions

Antonio Rojas Castro: Writing – original draft, Writing – review & editing. Frank Fischer and Julia Jennifer Beine reviewed the Preface. Ingo Börner contributed technical and editorial suggestions.

## 9. AI Use Declaration

The author used ChatGPT (OpenAI) to help revise this Preface and takes responsibility for the final text.

## 10. References

```{bibliography}
:filter: docname in docnames
```
## 11. Footnotes
[^notebooks]: The [DraCor Notebooks](https://dracor-org.github.io/dracor-notebooks/) {cite:p}`borner2026dracornotebooks` are a community-driven collection of Jupyter notebooks exploring further uses of the DraCor API. The notebooks are available in the [GitHub repository](https://github.com/dracor-org/dracor-notebooks).
