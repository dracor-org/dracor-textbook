---
title: "Front-end: Navigating DraCor"
myst:
  substitutions:
    chap_title: "Front-end"
author: "Antonio Rojas Castro"
date: "2026-04-09"
description: "This chapter explains how to use the DraCor front-end from the homepage to corpora and individual plays, with a tab-by-tab guide to Network, Speech distribution, Full text, Downloads and Tools."
keywords: ["DraCor", "front-end", "play page", "corpus page", "network", "speech distribution", "downloads", "Digital Humanities"]
license: "CC BY 4.0"
---


# Front-end: Navigating DraCor

```{admonition} Chapter metadata
:class: tip

**Author:** Antonio Rojas Castro   
**Version:** 0.7 (2026-11-25)  
**Review status:** Revised  
**Reviewers:** Julia Jennifer Beine; Frank Fischer
```

## 1. Overview

The DraCor front-end is an accessible starting point for exploring Programmable Corpora in DraCor. We start on the homepage, select a corpus, then open an individual play and explore its five tabs. In this introductory chapter, we use “play” as the practical term for the individual dramatic texts displayed in DraCor. Where “drama” appears, it refers more generally to dramatic literature as represented on the platform.

We work entirely in the DraCor web interface. We focus on what each view is designed to show and which interpretations it supports. Readers can follow a research question through the interface and download the relevant data for further analysis.

## 2. Requirements and Competences

* Web browser and internet access.
* Basic familiarity with plays (characters, acts/scenes) is helpful.

## 3. Learning Outcomes

After completing this chapter, learners will be able to:

1. Use the DraCor homepage to select a corpus and interpret the corpus summary cards.
2. Navigate a corpus page, search and filter its list of plays, and distinguish a permanent DraCor play ID from a slug.
3. Explain what each play tab (Network, Speech distribution, Full text, Downloads, Tools) is intended to show.
4. Interpret the Network and Speech distribution tabs at an introductory level.
5. Use the Full text tab to contextualise insights from the analytical tabs and to check text sources and segmentation.
6. Use the Downloads tab to retrieve outputs linked to specific semantic layers of a play.

## 4. Theoretical Background

DraCor presents drama as structured data. The front-end does not simply display a text: it renders several layers that are either encoded in the text itself (in TEI/XML format) or calculated from this encoding (for example, co-occurrence networks). This matters for interpretation. Each tab corresponds to a specific representation of the text, and the visualisations we see depend on modelling assumptions. In particular, the Network tab describes a co-occurrence rule: characters are linked if they speak in the same segment; if scene segmentation is unavailable, the act is used as the segment. For this reason, the front-end is best used as an exploratory environment: we can quickly form hypotheses, but we should make our observations traceable by noting which corpus and play we inspected and which tab produced a given view.

```{admonition} Tip for learners
When you write down an observation, include the corpus and DraCor play ID (shown in the header) and the tab you used. If the tab offers selectable methods or layers, note the selected option as well.
```

## 5. Practical Examples

### Example 1. Starting From the Homepage (Selecting a Corpus)

The homepage presents metadata for each corpus on a separate card. Examples include the French Drama Corpus (FreDraCor), German Drama Corpus (GerDraCor), English Drama Corpus (EngDraCor) and Russian Drama Corpus (RusDraCor). The cards combine a quick sense of scale (how many plays and characters a corpus contains) with token counts for different textual layers. These layer-specific counts are a useful reminder that drama is represented in multiple dimensions: running text, spoken text (marked up with `<sp>`) and stage directions (marked up with `<stage>`) can behave differently across corpora, depending on editorial practice and encoding. The cards also display a “last update” timestamp {cite:p}`borner2023cls{p. 58}` and the hash of the last commit in the GitHub repository. Recording the commit helps us refer to the specific corpus version used {cite:p}`borner2024cls{pp. 7–10}`. 

```{figure} ../images/front-end/home-page.png
---
alt: "DraCor homepage with corpus cards and summary statistics."
width: 100%
---
DraCor homepage. Corpus cards provide a high-level overview (plays, characters, token counts for text, character speech and stage direction, and a last update indicator). Accessed on 19 May 2026.
```

### Example 2. The Corpus Page (Searching and Selecting a Play)

The Calderón Drama Corpus (CalDraCor) page lists its plays in a searchable table. It also displays editorial credits, gives the latest commit hash and offers corpus metadata in JSON and CSV formats. The play table itself is the most practical entry point for reproducible selection: it lets us search, sort and identify each play by a stable play ID. When we move from browsing to documentation (for teaching, for collaboration or for later analysis), the play ID is more reliable than a title or filename alone, especially across corpora with variant spellings or multiple versions.

```{figure} ../images/front-end/cal-dracor.png
---
alt: "CalDraCor corpus page with a searchable play table and download buttons."
width: 100%
---
CalDraCor corpus page. The play table can be searched and sorted; corpus-level metadata can be downloaded as JSON or CSV; each play has a stable ID. Accessed on 19 May 2026.
```

### Example 3. The Play Page (Header and Tabs)

Play pages share a consistent header layout. In the example used in this chapter, *La vida es sueño* (*Life is a Dream*), the header shows the play title, the corpus badge (CalDraCor), a DraCor play ID and external identifiers, such as Wikidata QIDs for the play and author. These identifiers matter because they support unambiguous reference and interlinking across systems. Below the header, the play-level navigation tabs are visible: Network, Speech distribution, Full text, Downloads and Tools. In the rest of this chapter, we explain these five tabs in the given order.

The header displays the **DraCor play ID**, `cal000037`. This permanent identifier is unique across DraCor. Use the clipboard icon beside it to copy it. The URL for the play contains the **play name** (or **slug**), `la-vida-es-sueno`, which is also the TEI filename without the `.xml` extension. The play name is unique within its corpus, so we use it together with the corpus name, `cal`, to identify the play. In the API metadata for a play, `id` gives the DraCor play ID and `name` gives the play name {cite:p}`borner2023cls{§5.3.3}`. To document the version of the play data used in an analysis, record the corpus commit hash as well {cite:p}`borner2024cls{pp. 6–10}`.

#### Tab 1. Network

The Network tab provides a co-occurrence network for the play. A network consists of nodes that represent the characters and edges that represent co-occurrences. The interface states the modelling rule explicitly: if characters speak in the same scene or act (segment), they are linked. If there is no scene segmentation, characters that speak in the same act are linked {cite:p}`borner2023cls{pp. 25, 61}`. It is important to note that silent characters are not counted and that mere presence on stage is not evaluated. What we see first is a graph visualisation, which provides an immediate visual overview. This image is not only illustrative; it is also a reminder that the network is a specific representation of interaction derived from segmentation choices.

Next to the graph, DraCor summarises network properties in a compact panel. These values help us describe the network beyond what the eye can capture:

- **Segments**: the number of segments used to create co-occurrence links (the unit behind “same scene/act (segment)”).
- **All-in at segment *n* (at *x*%)**: the first segment by which all characters referenced in `<sp who>` have appeared at least once. They do not need to appear together. The percentage indicates the proportion of segments reached: for example, segment 21 out of 23 is approximately 91%.
- **Network size**: the number of speaking characters/entities in the play.
- **Density**: a value between 0 and 1 indicating how many of all possible edges between nodes are realised.
- **Diameter**: the highest value among all shortest distances between two nodes.
- **Average path length**: the average of all shortest path lengths between pairs of nodes in a connected network.
- **Average clustering coefficient**: a value between 0 and 1 indicating how strongly the network tends to form connected triplets (“triangles”).
- **Average degree**: the mean number of direct edges per node.
- **Maximum degree**: the largest number of direct connections any character has in the network.


The Network tab lists characters in order of first speech. Icons indicate a character’s sex or identify a character group, encoded in TEI as `<personGrp>`. This list provides a useful bridge to the text views: it invites us to check where a character first speaks and whether structural prominence in the network corresponds to speaking in the same segments as other characters. In *La vida es sueño*, five characters share the maximum degree of 12. The panel gives the number of characters in brackets. Alternatively, when one or two characters have the maximum degree, the panel shows their names.

```{figure} ../images/front-end/la-vida-es-sueno-network.png
---
alt: "Network tab showing a co-occurrence network and a panel of network properties."
width: 100%
---
Network tab. DraCor shows a co-occurrence network and summarises network properties (including the number of segments used to generate co-occurrence). Accessed on 19 May 2026.
```

#### Tab 2. Speech Distribution

The Speech distribution tab visualises how speech is distributed across the play. In the example shown, the interface offers multiple methods, selectable via radio buttons (for example, {cite:alp}`sapogov1974nekotorye`; {cite:alp}`yarkho2019speech`; {cite:alp}`fischer2017network`). This is a useful design choice because it makes clear that “speech distribution” is not a single universal measure but an operationalisation, that is, a way of turning a concept into a measurable procedure.

With the default Sapogov method selected, the line chart shows the segment number on the x-axis and the number of speaking characters on the y-axis. Two curves are displayed: one includes all characters, and one restricts the calculation to non-group characters only. Comparing these curves gives a quick sense of how character groups affect the apparent distribution and how “crowded” different parts of the play are. When we interpret this tab, it is worth keeping track of the selected method, because switching methods can change what the graph emphasises and, therefore, which comparisons are meaningful.

```{figure} ../images/front-end/la-vida-es-sueno-speech-distribution.png
---
alt: "Speech distribution tab with a plot and method selector."
width: 100%
---
Speech distribution tab. The interface offers different operationalisations (selectable methods) and can distinguish group characters from non-group characters. Accessed on 19 May 2026.
```
#### Tab 3. Full Text

The Full text tab displays the entire play, provides navigation by segment and identifies the source of the text. In the example below, the text is presented with structural markers (for example, “Jornada I”), with stage directions and speaker attributions and accompanied by a source note that indicates where the text was obtained from and how it was adapted.

A key feature of this tab is the Segments panel. It lists all segments and shows which characters speak in each one. This panel serves both as navigation and as an explicit representation of the segmentation that is the basis of other views, especially the co-occurrence network. For interpretive work, we therefore turn to the Full text tab to contextualise a pattern observed elsewhere: peaks in speech distribution or unexpectedly central characters in the network become more meaningful when we can locate the relevant passages.

```{figure} ../images/front-end/la-vida-es-sueno-full-text.png
---
alt: "Full text tab with provenance information and a segments navigation panel."
width: 100%
---
Full text tab. The full text of the play is displayed with provenance notes and a segment list that supports navigation and clarifies the segmentation used in related views. Accessed on 19 May 2026.
```

#### Tab 4. Downloads

The Downloads tab provides access to different semantic layers of a play in multiple formats. Readers can download the data behind a view and analyse them beyond the options available in the front-end. In the example below, network data may be downloaded in common network exchange formats (CSV, GEXF, GraphML). The tab also offers exports for spoken text (for example, JSON by character and plain text (`.txt`)), stage directions (with and without speaker names), the character list (CSV/JSON, including precalculated data) and the full TEI/XML-encoded text.

```{figure} ../images/front-end/la-vida-es-sueno-downloads.png
---
alt: "Downloads tab showing export options for network data, spoken text, stage directions, characters, and TEI/XML."
width: 100%
---
Downloads tab. DraCor provides exports for different semantic layers of a play (network data, spoken text, stage directions, character list and full TEI/XML-encoded text) in multiple formats. Accessed on 19 May 2026.
```

#### Tab 5. Tools

The Tools tab lets us send a selected text layer to an external service or open the character network in Gephi Lite. In the example below, we can select the text layer for analysis (Full text in TEI/XML, plain text, spoken text or stage directions) and then open third-party services, such as Voyant Tools or the CLARIN Language Resource Switchboard.

The main interpretive point here is that the selected layer shapes the results. Plain text and spoken text are typically more suitable for quick exploratory analyses in general-purpose tools, while TEI/XML-encoded text is better reserved for workflows that can process TEI/XML. For transparent reporting, it is sufficient to note which layer was selected and which tool was used, so that the external output can be understood as a transformation of a specific DraCor layer rather than as an abstract result detached from its source.

```{figure} ../images/front-end/la-vida-es-sueno-tools.png
---
alt: "Tools tab with external tool links and a text-layer selector."
width: 100%
---
Tools tab. The interface offers links to external tools and lets us choose which text layer (TEI/XML, plain, spoken, stage directions) is used for external analysis. Accessed on 19 May 2026.
```
## 6. Exercises

**Exercise 1. Identify Interface Layers (10–15 minutes)**
Choose one play and write 2–3 sentences per tab explaining which kind of representation it provides (network, distribution, text, exports, external tools).

Self-check: are you describing what is shown, rather than what you think it “means”?

**Exercise 2. Investigate the Relation Between the Network and Full Text Tabs (15–20 minutes)**
Pick one character that appears highly connected in the Network tab. Use the Segments panel in the Full text tab to locate two segments where this character and several other characters speak, and describe what is happening in those passages.

Self-check: can you point to specific segments that support your observation?

**Exercise 3. Downloads and Transparency (10–15 minutes)**
Download one file that corresponds to a view you used (for example, a network export). Note which semantic layer and which file format you chose, and why it matches your purpose.

Self-check: could someone else download the same file and understand what it represents?

```{admonition} Self-test
:class: tip
Open the [Self-test: Front-end](../assessment/04-front-end-assessment).
```


## 7. Teaching Notes

This chapter works well as a 60–90 minute in-person practical session, especially for students encountering DraCor for the first time. A useful structure is to begin with a short guided tour of the interface: homepage, corpus page, play page and the five main tabs (Network, Speech distribution, Full text, Downloads, Tools). The guided part should remain brief, since the aim is not to demonstrate every feature but to help students understand the logic of navigation and documentation. After this introduction, students can work in pairs on one selected play and complete a short “record note” including corpus, play ID, selected tab, chosen method or layer where relevant and one observation that could be checked by another student. This turns browsing into a reproducible practice and helps learners distinguish between what the interface shows and what they infer from it.

Lecturers may then organise a comparison activity around two or three plays, preferably from different corpora or with visibly different network and speech-distribution patterns. Each pair can report one observation from the Network tab and then verify or contextualise it in the Full text tab, using the Segments panel. This activity helps students see that visualisations are not independent evidence but derived views based on segmentation, encoded speakers, group characters and selected methods. A final plenary discussion can focus on modelling assumptions: what counts as a connection between characters? What happens when group characters are included or excluded? How does the selected speech-distribution method affect interpretation? What information is gained or lost when we move from text to network or chart?

For a longer session, this chapter can also be used as preparation for [Chapter 5, API: Working with DraCor Programmatically](05-api-working-with-dracor-programmatically) and [Chapter 6, DraCor in the Context of Research Infrastructures](06-dracor-in-the-context-of-research-infrastructures). After exploring the front-end, students can use the Downloads tab to retrieve one file that corresponds to a view they inspected, for example a network file, a character list, spoken text, stage directions or the TEI/XML source. They should document what semantic layer they downloaded, in which format and why that format would be useful for further work. This makes the transition from interface-based exploration to API-based or infrastructure-aware work more concrete: students first see a representation in the front-end, then identify the data layer behind it, and finally reflect on how that layer could be reused, analysed or questioned.

## 8. Further Reading and Resources 

For a detailed account of the front-end and its relationship to the API, see {cite:t}`borner2023cls{section 5.6, pp. 54–77}`. The report explains the corpus pages and play tabs as documented in 2023, providing technical background for the interface explored here.

For further work with character networks, {cite:t}`grandjean2015gephi` offers an accessible tutorial on network analysis and visualisation with Gephi. The study by {cite:t}`algee-hewitt2017distributed` shows how character networks can be used to rethink protagonism and mediation across corpora. The contribution by {cite:t}`beine2025how` presents a focused case study on role types, Roman comedy and early modern reception.

## 9. Glossary Entries

| Term | Definition |
| --- | --- |
| Average path length | The average of all shortest path lengths between pairs of nodes in a connected network. |
| Clustering coefficient | A value between 0 and 1 indicating how strongly nodes tend to form triangles, that is, tightly connected local clusters. |
| Co-occurrence network | Characters are represented as nodes (or vertices), and their co-occurrences as edges. In DraCor characters are linked if they speak in the same segment. If no scene segmentation is available, characters who speak in the same act are linked instead. Silent characters and mere stage presence are not taken into account. |
| DraCor play ID | A permanent identifier unique across DraCor, such as `cal000037` for La vida es sueño. It appears as `id` in the API metadata for a play. |
| Front-end | The web interface of DraCor. |
| Maximum degree | The largest number of direct connections any character has in the network. |
| Network density | A value between 0 and 1 indicating how many of all possible connections between nodes are realised. |
| Network diameter | The greatest shortest-path distance between any two nodes in the network. In other words, it is the longest of all minimal paths connecting pairs of characters. |
| Network size | The number of speaking characters/entities in a play. |
| Segment | A unit of segmentation used by the interface to structure co-occurrence and navigation. |
| Slug | The URL-friendly name of a play, such as `la-vida-es-sueno`. It is unique within its corpus and appears as `name` in the API metadata for a play. |


## 10. Next Steps

Continue with [Chapter 5](05-api-working-with-dracor-programmatically) to understand how the front-end relates to programmatic access and reproducible workflows.

## 11. AI Use Declaration

The author used Codex in ChatGPT Work Mode (OpenAI, GPT‑6) to receive feedback on the structure, language and editorial consistency of this chapter. The author reviewed, revised and approved the final text. No AI-generated output was used without human revision.

## 12. Author Contributions

Antonio Rojas Castro – conceptualisation, writing – original draft, methodology, visualisation, writing – review and editing.

## 13. References

```{bibliography}
:filter: docname in docnames
```
