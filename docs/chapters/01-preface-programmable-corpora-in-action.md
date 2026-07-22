---
title: "Preface: Programmable Corpora in Action"
myst:
  substitutions:
   chap_title: "Preface"
authors: "Antonio Rojas Castro"
date: "2026-07-21"
description: "This preface introduces the DraCor Textbook as an Open Educational Resource (OER), explains the concept of programmable corpora, outlines its target audiences and learning scenarios, and presents the main ways in which the textbook can be used for self-study and instructor-guided teaching."
keywords: ["DraCor Textbook", "programmable corpora", "Open Educational Resource", "active learning", "self-study", "Digital Humanities"]
license: "CC BY 4.0"
license link: "https://creativecommons.org/licenses/by/4.0/"
---

# Preface: Programmable Corpora in Action

```{warning}
This preface is a **draft**. It has not yet been proofread or formally reviewed. Content, terminology and examples may change.
```
```:class: tip
**Author:** Antonio Rojas Castro  
**Version:** 0.3 (2026-07-22)  
**Review status:** in progress  
**Planned reviewers:** members of the DraCorOS team and the DraCor Textbook editorial team
````

The **DraCor Textbook** is a curated, pedagogically structured Open Educational Resource (OER) developed by the DraCorOS and DraCor Textbook editorial teams. It provides a coherent introduction to working with programmable drama corpora in DraCor. Unlike the community-driven DraCor Notebooks, the textbook follows an explicit learning sequence and combines conceptual explanations with practical tasks, exercises and guidance for teaching.

## 1. DraCor and Programmable Corpora

DraCor is a research infrastructure for the collection, curation and computational analysis of drama corpora. A *programmable corpus* is not only a collection of digital texts. It also provides documented interfaces through which texts, metadata and derived data can be retrieved and processed automatically. In DraCor, openly available TEI/XML corpora are connected with a web front-end, an application programming interface (API) and analytical services. This combination supports both direct exploration and reproducible computational research {cite:p}`borner2023cls,borner2025cls`.

This preface introduces the purpose and scope of the textbook. The following chapters explain the individual components and workflows in greater detail, from corpus building and TEI encoding to the front-end, API-based access and local infrastructure.

## 2. Target Audience

```{figure} ../images/preface/target-audience.png
---
alt: "Diagram showing the target audience and possible uses of the DraCor Textbook."
width: 90%
---
The DraCor Textbook is designed for learners with little or no prior experience in Digital Humanities or programming and can be used for self-study or classroom teaching.
```

No previous programming experience is required. Chapters introduce technical concepts gradually and state their specific requirements at the beginning. Readers may follow the textbook sequentially or select individual chapters according to their learning or teaching context.

## 3. How to Use This Textbook

The DraCor Textbook supports two main learning scenarios: independent self-study and guided teaching or training. In both cases, it encourages active learning. Learners are not expected only to read about methods and tools. They are also invited to inspect data, navigate interfaces, encode texts, make API requests, compare results and reflect on the assumptions and limitations of each workflow.

### Self-Study

Learners working independently may follow the DraCor Textbook in sequence or begin with a chapter related to a specific interest. At the beginning of each chapter, the requirements and learning outcomes indicate what prior knowledge is expected and what learners should be able to understand or do after completing it.

The theoretical background introduces the main concepts, while the practical examples show how they are applied. Learners should reproduce these examples where possible and complete the exercises before proceeding to the self-test.

The self-tests are intended for formative feedback rather than grading. Answers are not stored, and the feedback explains why an option is correct or incorrect. When an answer is unclear, learners are encouraged to return to the relevant chapter section, interface or tool and verify the result. The glossary, Further Reading and Resources and Next Steps sections provide additional support for reviewing concepts or continuing with related topics.

### Classroom Teaching and Training

Instructors and trainers may use the textbook as the basis for a complete introductory course or select individual chapters and activities for shorter teaching units. The sequence, pace and level of technical detail can be adapted to the participants’ previous experience and the available teaching time.

The Teaching Notes at the end of each chapter suggest possible session formats, timings, group activities and discussion questions. These may include guided demonstrations, individual or paired exercises, comparisons between plays or corpora and collective reflection on modelling choices. The practical examples can first be presented by the instructor and then repeated or adapted by learners. Self-tests may be completed individually during or after a session and used to identify concepts that require further explanation.

In this scenario, the instructor does not only demonstrate procedures but also supports learners in formulating questions, documenting their decisions and distinguishing between what the data or interface shows and how these observations may be interpreted.

## 4. Exemplary Uses

The practical uses introduced in this Open Educational Resource correspond to the progression of its chapters:

<!-- The description of corpus building is based on the current Wiki outline and should be checked against Chapter 2 once the chapter draft is available. -->

- **building a drama corpus:** assembling, transforming and harmonising dramatic texts and metadata as a reusable, openly maintained corpus;
- **preparing texts in TEI/XML:** encoding the structure and features of dramatic texts according to the DraCor schema, using manual and semi-automatic workflows;
- **exploring corpora and plays through the front-end:** navigating corpus and play pages, interpreting networks and speech-distribution views, contextualising observations in the full text and retrieving available data layers;
- **working with DraCor programmatically:** using the interactive API documentation and Python to retrieve texts, metadata, character information and derived metrics, and to extend analysis from individual plays to complete corpora;
- **working with DraCor as research infrastructure:** understanding how its components interact and using Docker to run a local instance for custom corpora, controlled data versions and reproducible research.

Together, these uses guide learners from the preparation of structured textual data to its exploration, programmatic analysis and reproducible deployment. Each chapter also identifies the modelling choices, data dependencies and technical limitations relevant to its workflow.

## 5. Development Status

The DraCor Textbook is currently under development. A release candidate for the core content is planned for August 2026. Editorial guidelines, chapter templates and the ongoing development process are documented in the project repository and wiki.

## 6. References

```{bibliography}
:filter: docname in docnames
```
