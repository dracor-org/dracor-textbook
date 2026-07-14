::::{margin}
:::{admonition} Questions or feedback
:class: question-feedback

<a href="https://github.com/dracor-org/dracor-textbook/issues/new?labels=question&template=question.yml" class="external-link" target="_blank">
  Ask a question
</a><br>
<a href="https://github.com/dracor-org/dracor-textbook/issues/new?labels=feedback&template=feedback.yml" class="external-link" target="_blank">
  Give feedback
</a>

Your feedback helps us improve the textbook.
:::
::::


::::{margin}
:::{admonition} Citation
:class: citation-information

:::{literalinclude} /citation.bib
:language: bibtex
:::

Rojas Castro, Antonio; Börner, Ingo; Beine, Julia Jennifer; Skorinkin, Daniil; Trilcke, Peer; Fischer, Frank (2026). *DraCor Textbook*. https://github.com/dracor-org/dracor-textbook
:::
::::


# Preface: Programmable Corpora in Action

The **DraCor Textbook** is a curated, pedagogically structured Open Educational Resource (OER) developed by the DraCorOS and DraCor Textbook editorial teams. It provides a coherent introduction to working with programmable drama corpora in DraCor. Unlike the community-driven DraCor Notebooks, the textbook follows an explicit learning sequence and combines conceptual explanations with practical tasks, exercises and guidance for teaching.

## DraCor and Programmable Corpora

DraCor is a research infrastructure for the collection, curation and computational analysis of drama corpora. A *programmable corpus* is not only a collection of digital texts. It also provides documented interfaces through which texts, metadata and derived data can be retrieved and processed automatically. In DraCor, openly available TEI/XML corpora are connected with a web front-end, an application programming interface (API) and analytical services. This combination supports both direct exploration and reproducible computational research {cite:p}`borner2023cls,borner2025cls`.

This preface introduces the purpose and scope of the textbook. The following chapters explain the individual components and workflows in greater detail, from corpus building and TEI encoding to the front-end, API-based access and local infrastructure.

## Target Audience

```{figure} images/preface/target-audience.svg
---
alt: "Diagram showing the target audience and possible uses of the DraCor Textbook."
width: 90%
---
The DraCor Textbook is designed for learners with little or no prior experience in Digital Humanities or programming and can be used for self-study or classroom teaching.

No previous programming experience is required. Chapters introduce technical concepts gradually and state their specific requirements at the beginning. Readers may follow the textbook sequentially or select individual chapters according to their learning or teaching context.

## Exemplary Uses

The practical uses introduced in Book 1 correspond to the progression of its chapters:

<!-- The description of corpus building is based on the current Wiki outline and should be checked against Chapter 2 once the chapter draft is available. -->

- **building a drama corpus:** assembling, transforming and harmonising dramatic texts and metadata as a reusable, openly maintained corpus;
- **preparing texts in TEI/XML:** encoding the structure and features of dramatic texts according to the DraCor schema, using manual and semi-automatic workflows;
- **exploring corpora and plays through the front-end:** navigating corpus and play pages, interpreting networks and speech-distribution views, contextualising observations in the full text and retrieving available data layers;
- **working with DraCor programmatically:** using the interactive API documentation and Python to retrieve texts, metadata, character information and derived metrics, and to extend analysis from individual plays to complete corpora;
- **working with DraCor as research infrastructure:** understanding how its components interact and using Docker to run a local instance for custom corpora, controlled data versions and reproducible research.

Together, these uses guide learners from the preparation of structured textual data to its exploration, programmatic analysis and reproducible deployment. Each chapter also identifies the modelling choices, data dependencies and technical limitations relevant to its workflow.

## Structure and Development Status

Book 1 introduces the core concepts and workflows required to work with DraCor. Book 2 will extend this foundation through research-oriented case studies. The textbook can therefore serve both as a structured introduction and as a starting point for more specialised applications.

The textbook is currently under development. A release candidate for the core content is planned for August 2026. Editorial guidelines, chapter templates and the ongoing development process are documented in the project repository and wiki.

## References

```{bibliography}
:filter: docname in docnames
```
