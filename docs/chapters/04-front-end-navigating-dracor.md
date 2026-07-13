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

```{warning}
This chapter is a **draft**. It has not yet been proofread or formally reviewed.  
Content, terminology and examples may change.
```

```{admonition} Chapter metadata
:class: tip

**Version:** 0.6 (2026-05-19)  
**Review status:** Revised after internal review  
**Reviewer:** Julia Jennifer Beine
```

```{note}
**How to use this chapter:** We work entirely in the DraCor web interface. We begin on the homepage, move to a corpus page, and then explain each play tab (Network, Speech distribution, Full text, Downloads, Tools). Our goal is to make exploratory browsing precise enough that others may reproduce what we saw.
```

## 1. Overview

The DraCor front-end is the most accessible entry point to the programmable drama corpora in DraCor. It supports three key activities: discovering corpora and getting a quick statistical overview (homepage), browsing a corpus and selecting plays (corpus page), and inspecting a play through a set of tabs that expose text layers and derived analytical views (play page tabs). In this introductory chapter, we use “play” as the practical term for the individual dramatic texts displayed in DraCor. Where “drama” appears, it refers more generally to dramatic literature as represented in the platform.

In this chapter, we focus on what each view is for, what it shows, and what we can interpret safely. We treat the interface as a structured reading environment: a way to move from a research question to observations grounded in what is visible and can be downloaded.

## 2. Requirements and Competences

* Web browser and internet access.
* Basic familiarity with plays (characters, acts/scenes) is helpful.

## 3. Learning Outcomes

After completing this chapter, learners will be able to:

1. Use the DraCor homepage to select a corpus and interpret the corpus summary cards.
2. Navigate a corpus page, search and filter the list of plays, and recognise stable play identifiers.
3. Explain what each play tab (Network, Speech distribution, Full text, Downloads, Tools) is intended to show.
4. Interpret the Network and Speech distribution tabs at an introductory level.
5. Use the Full text tab to contextualise insights from the analytical tabs and to check text sources and segmentation.
6. Use the Downloads tab to retrieve outputs linked to specific semantic layers of a play.

## 4. Theoretical Background

DraCor presents drama as structured data. The front-end does not simply display a text: it renders several layers that are either encoded in the text itself (in TEI/XML format) or generated from this encoding (for example, co-occurrence networks). This matters for interpretation. Each tab corresponds to a specific representation of the text, and the visualisations we see depend on modelling assumptions. In particular, the Network tab describes a co-occurrence rule: characters are linked if they appear and speak in the same scene or act (segment). For this reason, the front-end is best used as an exploratory environment: we can quickly form hypotheses, but we should make our observations traceable by noting which corpus and play we inspected, and which tab produced a given view.

```{admonition} Tip for learners
When you write down an observation, include the corpus and play ID (from the URL or header) and the tab you used. If the tab offers selectable methods or layers, note the selected option as well.
```

## 5. Practical Examples

### Example 1. Starting From the Homepage (Selecting a Corpus)

On the DraCor homepage, we see corpus cards (for example, for FreDraCor, GerDraCor, EngDraCor, RusDraCor) that summarise each corpus at a glance. The cards combine a quick sense of scale (how many plays and characters a corpus contains) with token counts for different textual layers. These layer-specific counts are a useful reminder that drama is represented in multiple dimensions: running text, spoken text (marked up in TEI as `<sp>`), and stage directions (marked up in TEI as `<stage>`) can behave differently across corpora, depending on editorial practice and encoding. The cards also display a “last update” timestamp and the ID of the last commit in the GitHub repository {cite:p}`borner2024cls{pp. 7–12}`. Thus, this information helps situate the corpus as a living dataset and helps refer to the specific version used. 

```{figure} ../images/front-end/home-page.png
---
alt: "DraCor homepage with corpus cards and summary statistics."
width: 100%
---
DraCor homepage. Corpus cards provide a high-level overview (plays, characters, token counts for text, character speech and stage direction, and a last update indicator). Accessed 19 May 2026.
```

### Example 2. The Corpus Page (Searching and Selecting a Play)

A corpus page (example: CalDraCor) presents a searchable play table. Alongside editorial credits and the ID of the last commit, the interface typically offers corpus-level metadata downloads (for example, JSON and CSV). The play table itself is the most practical entry point for reproducible selection: it lets us search, sort, and identify each play by a stable play ID. When we move from browsing to documentation (for teaching, for collaboration or for later analysis), the play ID is more reliable than a title alone, especially across corpora with variant spellings or multiple versions.

```{figure} ../images/front-end/cal-dracor.png
---
alt: "CalDraCor corpus page with a searchable play table and download buttons."
width: 100%
---
CalDraCor corpus page. The play table can be searched and sorted; corpus-level metadata can be downloaded as JSON or CSV; each play has a stable ID. Accessed 19 May 2026.
```

### Example 3. The Play Page (Header and Tabs)

Play pages share a consistent header layout. In the example used in this chapter, *La vida es sueño* (*Life is a Dream*), the header shows the play title, the corpus badge (CalDraCor), a play ID, and external identifiers, such as Wikidata QIDs for the play and author. These identifiers matter because they support unambiguous reference and interlinking across systems. Below the header, the play-level navigation tabs are visible: Network, Speech distribution, Full text, Downloads and Tools. In the rest of this chapter, we explain these five tabs in the same order.

#### Tab 1. Network

The Network tab provides a co-occurrence network for the play. A network consists of nodes that represent the characters and edges that represent co-occurrences. The interface states the modelling rule explicitly: if characters speak in the same scene or act (segment), they are linked. If there is no scene segmentation, characters that speak in the same act are linked {cite:p}`borner2023cls{pp. 7–12, p. 51-53}`. It is important to note that silent characters are not counted and that mere presence on stage is not evaluated. What we see first is a graph visualisation, which provides an immediate visual overview. This image is not only illustrative; it is also a reminder that the network is a specific representation of interaction derived from segmentation choices.

Next to the graph, DraCor summarises network properties in a compact panel. These values help us describe the network beyond what the eye can capture:

- **Segments**: the number of segments used to create co-occurrence links (the unit behind “same scene/act (segment)”).
- **All-in at segment _n_ (at _x_%)**: the point in the play where the network has accumulated _x_% of its nodes, indicating how quickly the cast becomes present in the segmentation.
- **Network size**: the number of speaking characters/entities in the play.
- **Density**: a value between 0 and 1 indicating how many of all possible edges between nodes are realised.
- **Diameter**: the highest value among all shortest distances between two nodes.
- **Average path length**: the average of all shortest path lengths between pairs of nodes in a connected network.
- **Average clustering coefficient**: a value between 0 and 1 indicating how strongly the network tends to form connected triplets (“triangles”).
- **Average degree**: the mean number of direct edges per node.
- **Maximum degree**: the highest number of direct edges held by any single node (often shown with the character’s name).


The Network tab usually also includes a character list in order of appearance, sometimes with icons that indicate the sex of a character or mark character groups (marked up in TEI as `<personGrp>`). This list provides a useful bridge to the text views: it invites us to check where and how a character enters the play and whether structural prominence in the network corresponds to frequent co-presence in the segmented text.

```{figure} ../images/front-end/la-vida-es-sueno-network.png
---
alt: "Network tab showing a co-occurrence network and a panel of network properties."
width: 100%
---
Network tab. DraCor shows a co-occurrence network and summarises network properties (including the number of segments used to generate co-occurrence). Accessed 19 May 2026.
```

#### Tab 2. Speech Distribution

The Speech distribution tab visualises how speech is distributed across the play. In the example shown, the interface offers multiple methods, selectable via radio buttons (for example, {cite}`sapogov1974nekotorye`, {cite}`yarkho2019speech`, {cite}`fischer2017network`). This is a useful design choice because it makes clear that “speech distribution” is not a single universal measure but an operationalisation, that is, a way of turning a concept into a measurable procedure.

The plot shown in this view displays the scene (segment) number on the x-axis and the number of characters on the y-axis. Two curves are displayed: one includes all characters, and one restricts the calculation to non-group characters only. Comparing these curves gives a quick sense of how character groups affect the apparent distribution and how “crowded” different parts of the play are. When we interpret this tab, it is worth keeping track of the selected method, because switching methods can change what the graph emphasises and, therefore, which comparisons are meaningful.

```{figure} ../images/front-end/la-vida-es-sueno-speech-distribution.png
---
alt: "Speech distribution tab with a plot and method selector."
width: 100%
---
Speech distribution tab. The interface offers different operationalisations (selectable methods) and can distinguish group characters from non-group characters. Accessed 19 May 2026.
```
#### Tab 3. Full Text

The Full text tab provides a readable play text with navigation support, and it is also where provenance is made visible. In the example below, the text is presented with structural markers (for example, “Jornada I”), with stage directions and speaker attributions, and accompanied by a source note that indicates where the text was obtained from and how it was adapted.

A key feature of this tab is the Segments panel. It lists segments and shows which characters are present in each segment. This panel serves both as navigation and as an explicit representation of the segmentation that is the basis of other views, especially the co-occurrence network. For interpretive work, Full text tab, therefore, is where we turn to if we want to contextualise a pattern observed elsewhere: peaks in speech distribution or unexpectedly central characters in the network become more meaningful when we can locate the relevant passages quickly.

```{figure} ../images/front-end/la-vida-es-sueno-full-text.png
---
alt: "Full text tab with provenance information and a segments navigation panel."
width: 100%
---
Full text tab. The play text is displayed with provenance notes and a segment list that supports navigation and clarifies the segmentation used in related views. Accessed 19 May 2026.
```

#### Tab 4. Downloads

The Downloads tab provides access to different semantic layers of a play in multiple formats. This is the transparency layer of the front-end: it allows us to retrieve data that correspond to what we see in the interface. In the example below, network data may be downloaded in common graph exchange formats (CSV, GEXF, GraphML). The tab also offers exports for spoken text (for example, JSON by character and plain TXT), stage directions (with and without speaker names), the character list (CSV/JSON, often including precalculated data), and the full TEI/XML-encoded text.

```{figure} ../images/front-end/la-vida-es-sueno-downloads.png
---
alt: "Downloads tab showing export options for network data, spoken text, stage directions, characters, and TEI/XML."
width: 100%
---
Downloads tab. DraCor provides exports for different semantic layers of a play (network data, spoken text, stage directions, character list, and full TEI/XML-encoded text) in multiple formats. Accessed 19 May 2026.
```

#### Tab 5. Tools

The Tools tab links the play to external tools and lets us choose which textual layer should be routed to those tools. In the example below, we can select the text layer for analysis (Full text in TEI/XML, plain text, spoken text, or stage directions) and then open third-party services, such as Voyant Tools or the CLARIN Language Resource Switchboard. The tab also includes an entry point for network analysis via Gephi Lite.

The main interpretive point here is that the selected layer shapes the results. Plain text and spoken text are typically more suitable for quick exploratory analyses in general-purpose tools, while TEI/XML-encoded text is better reserved for workflows that can process TEI/XML. For transparent reporting, it is sufficient to note which layer was selected and which tool was used, so that the external output can be understood as a transformation of a specific DraCor layer rather than as an abstract result detached from its source.

```{figure} ../images/front-end/la-vida-es-sueno-tools.png
---
alt: "Tools tab with external tool links and a text-layer selector."
width: 100%
---
Tools tab. The interface offers links to external tools and lets us choose which text layer (TEI/XML, plain, spoken, stage directions) is used for external analysis. Accessed 19 May 2026.
```
## 6. Exercises

**Exercise 1. Identify interface layers (10–15 minutes)**
Choose one play and write 2–3 sentences per tab explaining which kind of representation it provides (network, distribution, text, exports, external tools).

Self-check: are you describing what is shown, rather than what you think it “means”?

**Exercise 2. Investigate the relation between the Network and Full text tabs (15–20 minutes)**
Pick one character that appears highly connected in the Network tab. Use the Segments panel in the Full text tab to locate two segments where this character addresses multiple other characters, and describe what is happening in those passages.

Self-check: can you point to specific segments that support your observation?

**Exercise 3. Downloads and Transparency (10–15 minutes)**
Download one file that corresponds to a view you used (for example, a network export). Note which semantic layer and which file format you chose, and why it matches your purpose.

Self-check: could someone else download the same file and understand what it represents?

```{admonition} Self-test
:class: tip
Open the [Self-test: Front-end](../assessment/03-front-end-assessment).
```


## 7. Teaching Notes

This chapter works well as a 60–90 minute in-person practical session, especially for students encountering DraCor for the first time. A useful structure is to begin with a short guided tour of the interface: homepage, corpus page, play page and the five main tabs (Network, Speech distribution, Full text, Downloads, Tools). The guided part should remain brief, since the aim is not to demonstrate every feature but to help students understand the logic of navigation and documentation. After this introduction, students can work in pairs on one selected play and complete a short “record note” including corpus, play ID, selected tab, chosen method or layer where relevant, and one observation that could be checked by another student. This turns browsing into a reproducible practice and helps learners distinguish between what the interface shows and what they infer from it.

Lecturers may then organise a comparison activity around two or three plays, preferably from different corpora or with visibly different network and speech-distribution patterns. Each pair can report one observation from the Network tab and then verify or contextualise it in the Full text tab, using the Segments panel. This activity helps students see that visualisations are not independent evidence but derived views based on segmentation, encoded speakers, group characters, and selected methods. A final plenary discussion can focus on modelling assumptions: what counts as a connection between characters? What happens when group characters are included or excluded? How does the selected speech-distribution method affect interpretation? What information is gained or lost when we move from text to network or chart?

For a longer session, this chapter can also be used as preparation for Chapters 5 and 6. After exploring the front-end, students can use the Downloads tab to retrieve one file that corresponds to a view they inspected, for example a network file, a character list, spoken text, stage directions, or the TEI/XML source. They should document what semantic layer they downloaded, in which format, and why that format would be useful for further work. This makes the transition from interface-based exploration to API-based or infrastructure-aware work more concrete: students first see a representation in the front-end, then identify the data layer behind it, and finally reflect on how that layer could be reused, analysed or questioned.

## 8. Further Reading and Resources 

- Grandjean’s tutorial {cite}`grandjean2015gephi` offers an accessible introduction to network analysis and visualisation with Gephi.
- Algee-Hewitt’s study {cite}`algee-hewitt2017distributed` shows how character networks can be used to rethink protagonism and mediation across corpora.
- Beine’s contribution {cite}`beine2025how` presents a focused case study on role types, Roman comedy and early modern reception.


## 9. Glossary

| Term | Definition |
| --- | --- |
| Front-end | The web interface of DraCor. |
| Play ID (slug) | A stable identifier for a play (visible in the header/URL and in corpus tables). |
| Segment | A unit of segmentation used by the interface to structure co-occurrence and navigation. |
| Co-occurrence network | Characters are represented as nodes (or vertices), and their co-occurrences as edges. In DraCor characters are linked if they speak in the same segment. If no scene segmentation is available, characters who speak in the same act are linked instead. Silent characters and mere stage presence are not taken into account. |
| Network size | The number of speaking characters/entities in a play. |
| Network diameter | The greatest shortest-path distance between any two nodes in the network. In other words, it is the longest of all minimal paths connecting pairs of characters. |
| Network density | A value between 0 and 1 indicating how many of all possible connections between nodes are realised. |
| Clustering coefficient | A value between 0 and 1 indicating how strongly nodes tend to form triangles, that is, tightly connected local clusters. |
| Average path length | The average of all shortest path lengths between pairs of nodes in a connected network. |
| Maximum degree | The highest number of direct connections held by any single node (often shown with the character’s name). |


## 10. Next Steps

* Continue with: [Chapter 5 (API)](05-api-working-with-dracor-programmatically) to understand how the front-end relates to programmatic access and reproducible workflows.

## 11. AI Use Declaration

The author used ChatGPT to receive feedback on the structure, language and editorial consistency of this chapter. The author reviewed, revised and approved the final text. No AI-generated output was used without human revision.

## 12. Author Contributions

Antonio Rojas Castro: conceptualisation, writing: original draft, methodology, visualisation, writing: review and editing.

## 13. References

```{bibliography}
:filter: docname in docnames
```
