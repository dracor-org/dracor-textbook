---
title: "Corpus Building in DraCor"
myst:
  substitutions:
   chap_title: "Corpus Building in DraCor"
authors: "Daniil Skorinkin; Julia Jennifer Beine"
date: "2026-08-21"
description: "In this chapter, we describe how the existing corpora in DraCor have been built. In most cases, the corpus building has started by inventorying available online resources while applying certain selection criteria. We elaborate on these selection criteria, illustrated by the resulting DraCor corpora."
keywords: ["programmable corpora", "corpus building", "corpus archaeology"]
licence: CC BY 4.0
licence link: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
---


# Corpus Building in DraCor

```{warning}
This chapter is a **draft**. It has not yet been proofread or formally reviewed. Content, terminology, and examples may change.
```

```{admonition} Chapter metadata
   :class: tip    
         
    **Authors:** Daniil Skorinkin; Julia Jennifer Beine     
    **Version:** 0.1 (2026-08-21)
    **Review status:** not yet reviewed      
    **Planned reviewers:** Antonio Rojas Castro; Frank Fischer
```

## 1. Overview

In this chapter, we describe how the existing corpora in DraCor have been built. In most cases, the corpus building has started by inventorying available online resources while applying certain selection criteria. We elaborate on these selection criteria, illustrated by the resulting DraCor corpora.

## 2. Requirements and Competences

* Web browser and internet access required.

## 3. Learning Outcomes

After completing this chapter, learners will be able to:
1. Describe the principles and focuses of corpus building in DraCor.
2. Describe the types of sources of the existing DraCor corpora.

## 4. Theoretical Background

### 4.1. Distributed Corpus Building

DraCor is a collaborative, community-driven project. While a core team at several universities maintains the shared platform – the Application Programming Interface (API), the front-end, the text encoding schema – the corpora themselves come from a wide variety of contributors. Individual scholars, research groups, and digital humanities projects across many countries build, maintain, and contribute corpora. In building the corpora, scholars may pursue their own research questions (also see {cite:t}`schoech2017aufbau{p. 224}`). This distributed model of corpus building {cite:p}`giovannini2023distributed` is one of the crucial characteristics of DraCor and, at the same time, an important factor shaping the diversity and heterogeneity of the DraCor corpora. The common ground is that all DraCor corpora include dramatic texts. In the following chapters, we will look at the DraCor corpora from different perspectives, considering their selection criteria and focuses as well as their sources.

### 4.2. Sources of the Corpora

In DraCor, most corpus builders follow an opportunistic approach, inventorying available online resources while applying certain selection criteria (on the different types of corpus building, see {cite:t}`schoech2017aufbau{pp. 225–226}`). Overall, the DraCor corpora may be divided into two broad types of corpora, based on how they were built: imported and in-house corpora.

The first type is collections that already existed as standalone digital projects and were subsequently converted to the DraCor format and integrated into the platform. The DraCor format is files in e**X**tensible **M**arkup **L**anguage (XML) that follow the encoding guidelines by the **T**ext **E**ncoding **I**nitiative (TEI)  (see chapter 2 “TEI Encoding: Preparing Texts for Programmable Corpora”) and also adhere to the DraCor TEI schema. When importing existing text collections, the selection of dramatic texts was not made by the DraCor team; it was determined by the scope and criteria of the original project. The role of the DraCor team was primarily one of format conversion and homogenisation. A prominent example is the French Drama Corpus (FreDraCor, {cite:t}`milling2021ff.french`), which is derived entirely from Paul Fièvre’s “Théâtre Classique” project {cite:p}`fievre2007-presenttheatre`, a long-running, meticulously curated collection of dramatic texts from French classicism. Similarly, the Shakespeare Drama Corpus (ShakeDraCor, {cite:t}`dracor2018-presentshakespeare`) inherits its texts from the digital editions of the Folger Shakespeare Library {cite:p}`folgershakespeare`; the Swedish Drama Corpus (SweDraCor, {cite:t}`dracor2018-presentswedish`) takes its texts from the “eDrama” project {cite:p}`forsbomedrama`; the English Drama Corpus (EngDraCor, {cite:t}`giovannini2024ff.english`) is almost entirely based on TEI/XML files from the “EarlyPrint” project {cite:p}`muellerearlyprint`; and the Greek Drama Corpus (GreekDraCor {cite:t}`beine2019-presentgreek`) and Roman Drama Corpus (RomDraCor, {cite:t}`beine2024just`) both draw on the “Perseus Digital Library” {cite:p}`crane[1994-present]perseus` to provide the extant ancient plays. Note that GreekDraCor additionally features a play from Wikisource.

The second type is in-house corpora – collections that were built specifically for DraCor by its maintainers, drawing on multiple digital sources and sometimes even newly digitised materials. Here, the DraCor corpus maintainers themselves decide which plays to include, based on criteria of their own choosing. The corpus grows organically over time as new texts are found, encoded, and added. The German Drama Corpus (GerDraCor) is the most prominent example: it began with plays from the TextGrid Repository {cite:p}`textgridconsortiumtextgrid, fischer2015introducing, fischer2015not, fischer2015working`, but has since expanded to include texts from over a dozen different digital sources, such as Wikisource {cite:p}`wikisource2003-presentwikisource`, Projekt Gutenberg-DE {cite:p}`latusseck1994-presentprojekt`, Google Books {cite:p}`google[2004-present]google`, Deutsches Textarchiv {cite:p}`deutschestextarchiv[2007-present]deutsches`, the Internet Archive {cite:p}`internetarchive[1996-present]internet`, and various academic libraries. The Russian Drama Corpus (RusDraCor, {cite:t}`fischer2020-presentrussian`) was similarly assembled from a range of Russian online libraries, such as [lib.ru](http://lib.ru) {cite:p}`moshkowbiblioteka`, [ilibrary.ru](http://ilibrary.ru) {cite:p}`komarovinternetbiblioteka`, [rvb.ru](http://rvb.ru) {cite:p}`russkayavirtualnayabibliotekarusskaya`, [feb-web.ru](http://feb-web.ru) {cite:p}`fundamentalnayaelektronnayabibliotekafundamentalnaya`, and Wikisource {cite:p}`wikisource2003-presentwikisource`. The Dutch Drama Corpus (DutchDraCor, {cite:t}`vanderdeijl2023-presentdutch`) derives most of its plays from the “Digitale Bibliotheek voor de Nederlandse Letteren” (DBNL, {cite:t}`taalunie[1999-present]digitale`), plus a handful of texts added from the “Ceneton” project {cite:p}`harmsen[1992-present]census, harmsen2007ceneton`. The Ukrainian Drama Corpus (UDraCor, {cite:t}`tokarskyi2022ff.ukrainian`) draws on UkrLib online library {cite:p}`ukrlib`, dedicated editions of individual authors, and several other Ukrainian digital sources, such as [litopys.org.ua](http://litopys.org.ua) {cite:p}`litopys-ua` and [myslenedrevo.com.ua](http://myslenedrevo.com.ua) {cite:p}`myslenedrevo`. The Polish Drama Corpus (PolDraCor, {cite:t}`pastuch2023-presentpolish`) combines materials mainly from Polona (the Polish national digital library, {cite:t}`polona`), with a few plays from other Polish library platforms. 

In practice, the boundary between imported and domestic corpora is not always sharp. Some corpora started as imports from a single project but were later supplemented with plays from other sources, making them hybrids. For instance, the Italian Drama Corpus (ItaDraCor, {cite:t}`fischer2020-presentitalian`) draws roughly 95% of its texts from the “Biblioteca Italiana” {cite:p}`sapienzauniversitadiroma[2000-present]biblioteca`, with occasional additions from Google Books, the Internet Archive, and Wikisource. Still, the imported-versus-domestic distinction captures a crucial and consequential difference: it determines whether the DraCor curators could freely choose how to build their corpus or were constrained by the selection decisions of a source project.

### 4.3. Scope of the Corpora

On a more fine-grained level, DraCor corpora differ in their selection criteria. All DraCor corpora share a genre-specific selection criterion, as they only include dramatic texts. Further selection criteria may be a certain time period, a certain region of production, a certain language, or a certain author (also see {cite:t}`schoech2017aufbau{p.224}`).

**Language** is by far the most common selection criterion. The majority of DraCor corpora provide plays originally written in a particular language, regardless of the authors’ nationality, the creation period, or the place of publication. GerDraCor, for instance, includes German-language dramas by authors from what is now Germany, Austria, and Switzerland, spanning from the 1530s to the 1940s. RusDraCor contains dramas written in Russian by citizens of the Russian Empire and the Soviet Union (whose ethnic identity might or might not be Russian in a narrow sense). The Romanian Drama Corpus (RoDraCor, {cite:t}`terian2025-presentromanian`) collects Romanian-language dramas; the Hungarian Drama Corpus (HunDraCor, {cite:t}`departmentofdigitalhumanitiesateotvosloranduniversity2021-presenthungarian`) Hungarian ones; the Polish Drama Corpus (PolDraCor) Polish ones; and so on. Language-specific corpora form the largest corpora group in DraCor.

An adjacent case is a corpus whose scope is a dialect or a regional variety of a language. The Alsatian Drama Corpus (AlsDraCor, {cite:t}`ruizfabo2019-presentalsatian`) comprises plays written in Alsatian, which is variously classified as a dialect of Alemannic German or as a language in its own right – a useful reminder that the line between “language” and “dialect” is often more political and cultural than strictly linguistic. The Argentinian Drama Corpus (ArDraCor, {cite:t}`ardracor`) presents a related but different kind of boundary question: it collects plays written in Spanish, but specifically by Argentinian authors, reflecting a decision by its creators to treat Argentinian dramatic literature as a distinct cultural tradition rather than folding it into a pan-Hispanic corpus {cite:p}`abordajes2026`. Here, the selection criterion is better described as national culture or place of production rather than language alone.

Some corpora combine language and time period as joint selection criteria. GreekDraCor is not a corpus of all drama ever written in Greek; it is a corpus of **ancient** Greek drama – the tragedies and comedies of classical Athens. Similarly, RomDraCor focuses on **ancient** Roman drama (Plautus, Terence, Seneca), not on Latin drama in general. The Neo-Latin Drama Corpus (NeoLatDraCor) complements RomDraCor by collecting dramatic texts written in Latin starting from the early-modern period. The Spanish Drama Corpus (SpanDraCor) is also limited by both language (Spanish) and period (1868–1936), since it inherits the temporal boundaries of the “BETTE” corpus {cite:p}`calvo2017ghedi` from which it derives.

Finally, a few DraCor corpora are defined by authorship as they contain the dramatic works of a single playwright. ShakeDraCor is the most prominent example, bringing together Shakespeare’s 37 plays from the Folger Shakespeare Library editions. The Calderón Drama Corpus (CalDraCor, {cite:t}`ehrlicher2019-presentcalderon`) collects the comedies of Pedro Calderón de la Barca. The German Shakespeare Drama Corpus (GerShDraCor, {cite:t}`fischer2021-presentgerman`) is a special case: it contains Shakespeare’s plays in the canonical German translation by the translator group around August Wilhelm Schlegel and Ludwig Tieck, making it an author-focused corpus that simultaneously documents a major act of cultural transfer (also see {cite:t}`beine2017re`). The Ibsen Drama Corpus (IbsDraCor, {cite:t}`centreforibsenstudies2025-presentibsen`) collects all of Henrik Ibsen’s dramatic works from the scholarly edition “Henrik Ibsen’s Writings” maintained by the Centre for Ibsen Studies at the University of Oslo.

It is worth noting that these categories are not mutually exclusive. A language-based corpus like GerDraCor implicitly spans several centuries and many authors; an author-based corpus like ShakeDraCor is also implicitly a period corpus (roughly 1590–1613) and a language corpus (English). The previous explanations focused on the **primary** selection criterion – the principle that first determines what is included and what is not.

### 4.4. Source Types of the DraCor Corpora From the Technical Viewpoint

TEI/XML encoding in DraCor requires that the dramatic text is available in digital form. This text can either come from a pre-existing digital resource – an online library, a text collection, a digital archive – or it can be digitised from a print source such as a book or a manuscript. In the vast majority of cases, DraCor corpora are the result of what we might call **secondary digital processing**: the plays have already undergone primary digitisation by someone else (a library, a scholarly project, a volunteer community), and the DraCor encoding work consists of converting those existing digital texts into the DraCor TEI/XML format. Only in a minority of cases are plays digitised from print sources specifically for inclusion in DraCor.

The type of digital source significantly influences the process of corpus building, because sources differ enormously in the extent of usable structural markup they already contain. The following overview captures the main source types, roughly ordered from the sources easiest to include in a DraCor corpus to those more difficult to incorporate.

**TEI/XML sources.** The most straightforward scenario is when the source texts are already encoded in TEI/XML and provide at least the core dramatic structure: acts, scenes, speakers, speech, and stage directions. This was the case for the TextGrid Repository texts that seeded GerDraCor, for the Théâtre Classique files behind FreDraCor, for the Folger Shakespeare editions in ShakeDraCor, for the eDrama files in SweDraCor, for the EarlyPrint files in EngDraCor, and for many texts in DutchDraCor (via DBNL). However, “TEI/XML” is a broad standard. Despite being nominally standardised, these sources differ considerably in the granularity of their markup, in how strictly they followed the TEI guidelines, which version of the TEI schema they used, and how they split texts across files. In TextGrid, for example, Goethe’s “Faust” was stored as five separate TEI documents, and some plays counted double due to co-authorship metadata. These inconsistencies require substantial homogenisation work using e**X**tensible **S**tylesheet **L**anguage **T**ransformations (XSLT) or Python scripts, and manual editing. Most recently, Large Language Models (LLMs) have also been used to assist with certain encoding tasks.

**Structured non-TEI markup.** In many cases, source texts come not as TEI/XML but in some other format that encodes the structural properties of plays in a consistent, semi-machine-readable way. The **H**ypertext **M**arkup **L**anguage (HTML) is the most common example. Online libraries typically display plays as HTML pages, and while HTML was designed for visual presentation rather than semantic encoding, it often distinguishes consistently between spoken text and stage directions, marks act and scene headings as different levels of header, and wraps speaker names in recognisable formatting. Exploiting this structural regularity, the DraCor corpus builders may write conversion scripts to produce a first TEI draft that requires only moderate manual correction. This has been the approach for many plays in RusDraCor (sourced from online libraries like ilibrary.ru and rvb.ru), for UDraCor (with plays from ukrlib.com.ua), and for plays sourced from various national digital libraries. DOCX/DOC files with consistent formatting represent a similar case: the formatting (styles, bold text, indentation) can carry structural information that aids conversion. NeoLatDraCor has developed a related From Word to TEI workflow {cite:p}`beine2024ff.neolatin`.

**Weakly structured or plain text.** Sometimes a play is available as an HTML document whose tags are inconsistent or carry no useful structural information, or as mere plain text. In the most fortunate plain-text cases, the text may still contain rudimentary implicit markup, such as speaker names in capital letters, stage directions in brackets, consistent blank lines between scenes, that may be exploited with regular expressions to automate part of the encoding. In less fortunate cases, the encoding must be done largely by hand. Some plays in DutchDraCor, for example, were sourced from the Ceneton project {cite:p}`harmsen[1992-present]census, harmsen2007ceneton`, whose HTML was too inconsistent to be converted to TEI automatically; the text was stripped to raw form and re-encoded from scratch using a combination of regular expressions and manual work.

**Digital images (OCR required).** Some plays are only available as page images, for instance, as PDF files without a text layer, or as scanned pages in a digital library. In these cases, **O**ptical **C**haracter **R**ecognition (OCR) had to be performed first to extract the text, which then required correction – OCR output for older typefaces and historical orthography is rarely clean – before TEI encoding could begin.

**Print sources (scanning and OCR).** In the rarest cases, the DraCor corpus maintainers digitise plays from physical print sources: scanning the pages, performing OCR, correcting the output, and then encoding the text in TEI/XML. In very rare cases, corpus builders may also include manuscript sources from scratch, using **H**andwritten **T**ext **R**ecognition (HTR). This is the path of last resort, used only for dramatic texts that existed in no digital form at all.

It should be noted that a single corpus often draws on sources of several different types. GerDraCor is a good example: the majority of its plays (528 out of 768 as of early 2026) comes from the TextGrid Repository as TEI/XML, but the corpus also includes 115 plays sourced from Google Books (typically as scanned page images requiring OCR), 39 from Projekt Gutenberg-DE, 32 from Wikisource, and smaller numbers from the Berlin State Library {cite:p}`staatsbibliothekzuberlindigitalisierte`, Deutsches Textarchiv, the Internet Archive, and various academic libraries – each with its own format and its own conversion challenges.

## 5. Practical Examples

### 5.1. Example A: The Building of GerDraCor[^information]

GerDraCor is the oldest and one of the most extensively documented corpora in DraCor. Its history illustrates many of the general principles discussed above – the role of inherited collections, the gradual expansion from a single source to many, and the nature of corpus curation as an ongoing process. Because its development is closely intertwined with the origins of the DraCor platform itself, telling the story of GerDraCor is also, in part, telling the story of how DraCor came to be.

The roots of GerDraCor lie in the DLINA project (Digital Literary Network Analysis, {cite:t}`dlina_blog_2017`), a research group whose members included Frank Fischer, Mathias Göbel, Dario Kampkaspar, Christopher Kittel, and Peer Trilcke. The goal of DLINA was to study the network structure of dramatic texts (who appears on stage together with whom), using computational methods. In order to do so, the group needed a large, consistently encoded corpus of German-language plays.

The starting point was the TextGrid Repository {cite:p}`textgridconsortiumtextgrid`, the largest freely available TEI-encoded collection of German literature that contains thousands of texts released under a CC BY licence. But extracting the dramatic texts from TextGrid turned out to be a challenge {cite:p}`fischer2015not`. The seemingly straightforward query “How many dramatic texts are in the TextGrid Repository?” led through a thicket of complications: multi-part works stored as separate TEI documents (Goethe’s “Faust” was split into five files, Wagner’s “Ring” into four); doublets caused by co-authorship metadata (a play by two authors was counted twice because each author’s file contained a reference to it); and inconsistencies in genre classification. After systematic cleaning using **X**ML **Query** Language” (XQuery) against an eXist-db instance, the DLINA team arrived at 666 dramatic texts.

From these 666 texts, the team then selected 465 plays to form the DLINA Corpus 15.07 (Codename: Sydney), named after the DH2015 conference in Sydney, where the results would be presented. The selection criteria narrowed the corpus to a specific period and type {cite:p}`fischer2015introducing`:

* The temporal scope began with the German Enlightenment, specifically with Gottsched’s “Der sterbende Cato” (printed 1732), a widely recognised turning point in the history of German drama. This meant discarding 147 pre-Gottsched texts.
* Foreign-language originals and translations were excluded – the corpus was to contain only works originally written in German.
* Pantomime plays lacking speech elements (`<sp>`) were discarded, since they could not be analysed for dramatic dialogue.
* Fragments – texts clearly left unfinished by their authors – were removed.

A further 32 texts were sorted out during editing because of severely defective TEI markup, because they turned out to be fragments that had been overlooked, or because their dramatic structure was too complex for the initial project tools to handle {cite:p}​`fischer2015introducing`.

The DLINA project also had to deal with inconsistent metadata {cite:p}`fischer2015working`. The date information in the TextGrid Repository was unreliable – sometimes the `<creation>` element was empty, sometimes it contained only the author’s birth and death years as a vague bracket. The team developed a pragmatic decision tree: first, look for an exact year in the `<creation>` element; if unavailable, take the earliest year mentioned in the `<note>` element (which often contained information about first print or premiere dates); and as a last resort, use the author's year of death as a terminus ante quem. These approximate dates were encoded into filenames (e.g. `1772-Lessing_Gotthold_Ephraim-Emilia_Galotti-lina.xml`) to enable chronological sorting – a practical workaround that the team openly described as an approximation, not a substitute for proper metadata curation.

For their network analysis, the DLINA team did not initially need the full texts; they worked with a custom intermediate format they called the “Zwischenformat”, which stored only metadata and detailed structural information about acts, scenes, and which characters appeared in which segment. This was sufficient for extracting co-presence networks. The full texts from TextGrid were preserved alongside the “Zwischenformat” files, but were not the primary object of analysis at this stage {cite:p}​`kampkaspar2015zwischenformat`.

On 2 December 2016, Mathias Göbel – during a hackathon at the University of Potsdam – made the first commit to what would become the GerDraCor repository on GitHub {cite:p}`borner2024cls`{p. 13}. This initial commit added 465 TEI/XML files (one per play) to a `data` folder. The commit message reads: “inital commit: converted text based on LINA and TextGrid.” The files combined the full text from the TextGrid Repository sources with metadata from the DLINA “Zwischenformat”, now encoded following the TEI Guidelines rather than the custom format of the project.

This moment marks the “birth” of GerDraCor as a distinct entity, though it would take until 2017/2018 for the corpus to become fully integrated into the emerging DraCor platform. In September 2017, two significant organisational commits reshaped the repository: the data folder was renamed from `data` to `tei` (establishing the convention used across all DraCor corpora), and all filenames were standardised to match the `playname` identifier format (e.g. `lessing-emilia-galotti.xml` instead of `1772-Lessing_Gotthold_Ephraim-Emilia_Galotti-lina.xml`).

Throughout 2017, the corpus remained stable at 465 plays – no new texts were added, though the existing files underwent significant internal changes (markup homogenisation, formatting). The first sign of growth beyond the original TextGrid seed came on 6 January 2018, when a play not derived from TextGrid was added for the first time: “Die Überschwemmung” by Franz Philipp Adolph Schouwärt, converted from Wikisource. This small event – one play from one new source – marked the beginning of GerDraCor’s transformation from a static inherited collection into a living, actively curated corpus {cite}`borner2024cls`{p. 15}.

The growth accelerated markedly from 2020 onwards. As documented in the CLS INFRA D7.3 report by Börner and Trilcke {cite}`borner2024cls`{p. 15}, the number of plays added per year increased substantially:

| Year | New plays | Cumulative total |
|------|-----------|------------------|
| 2016 | 465       | 465              |
| 2017 | 0         | 465              |
| 2018 | 7         | 472              |
| 2019 | 7         | 479              |
| 2020 | 41        | 520              |
| 2021 | 32        | 552              |
| 2022 | 45        | 597              |
| 2023 | 66        | 663              |
| 2024 | 15        | 678              |

By March 2026, GerDraCor contains 768 plays from over a dozen different digital sources. The TextGrid Repository remains the largest single contributor (528 plays), but Google Books has become the second-largest source (115 plays), followed by Projekt Gutenberg-DE (39), Wikisource (32), the Berlin State Library (9), Project Gutenberg (9), a scholarly edition of Marie von Ebner-Eschenbach (9), Deutsches Textarchiv (4), and smaller numbers from the Internet Archive, the Göttingen State and University Library, the Herzogin-Anna-Amalia-Bibliothek, and several other academic libraries [^play-number].

This diversification of sources also brought an expansion of the temporal scope of the corpus. The original DLINA selection had focused on the period from the German Enlightenment (1730s) through the early 20th century. As new plays were added from different sources, GerDraCor grew to cover German-language drama from the 1530s to the 1940s – a much broader span that now includes Renaissance and early Baroque texts as well as works from the Weimar Republic era {cite:p}​borner2024cls​{pp. 16–17}.

It is important to understand that the evolution of a living corpus like GerDraCor is not only a matter of adding new plays. The existing files also change over time – sometimes substantially. The CLS INFRA D7.3 report identifies several categories of change {cite:p}`borner2024cls`{p. 20}:

**Batch edits** affect all files in the corpus simultaneously. Major examples include the addition of Wikidata identifiers to all plays (September 2018), the replacement of DLINA-era identifiers with DraCor IDs (May 2019), the introduction of a RelaxNG schema reference (September 2019), the normalisation of genre terms and introduction of Wikidata-linked genre classification (December 2020), and the addition of a `<standOff>` element for contextual metadata (May 2022). Each of these batch edits represents a structural evolution of the encoding, often driven by new features being developed in the DraCor API {cite:p}`borner2024cls`{pp. 20–24}.

**Individual file edits** correct errors, enrich metadata, or improve the encoding of specific plays. The D7.3 report traces the file for Lessing’s “Emilia Galotti” through 26 distinct versions, documenting changes that range from the addition of text formatting (line breaks and indentation) in the earliest commits to the gradual enrichment of the TEI header with Wikidata links, genre information, and character relation data {cite:p}`borner2024cls`{pp. 18–20}.

**Encoding of character relations** – social and family relationships between dramatic characters – was introduced to GerDraCor between September and November 2019, in cooperation with the QuaDramA project {cite:p}`reiter[2017-present]quadrama`. This feature was added to 358 plays, not all at once but file by file, illustrating how new encoding features can enter a corpus incrementally rather than through a single batch operation.

This ongoing evolution is what makes GerDraCor a “living corpus” in the full sense of the term: it is not merely a collection that grows by accretion, but one whose individual components are themselves subject to continuous revision and enrichment. For researchers working with GerDraCor, this has practical implications for reproducibility – a topic addressed in detail in the CLS INFRA D7.3 report, which recommends citing specific Git commits as stable references to particular states of the corpus {cite:p}`borner2024cls`{p. 32}.

## 6. Exercises

### Exercise 1: Imported and In-house Corpora

```{admonition} Assessment
:class: tip
Open the [Assessment: Corpus Building in DraCor](../assessment/02-corpus-building-in-dracor-assessment.md#exercise-1-imported-and-in-house-corpora).
```

### Exercise 2: Selection Criteria in Corpus Building

```{admonition} Assessment
:class: tip
Open the [Assessment: Corpus Building in DraCor](../assessment/02-corpus-building-in-dracor-assessment.md#exercise-2-selection-criteria-in-corpus-building).
```

## 7. Teaching Notes

Lecturers may select DraCor corpora not discussed in this chapter and ask their students to research how the corpora have been built, preferably in small groups of two. Note that a basic knowledge of the DraCor front-end may be useful, e.g. how to find the editorial information of a corpus in the front-end (or GitHub) or related publications in the DraCor research bibliography. Thus, lecturers may include [Chapter 4, “Front-End: Navigating DraCor”](https://github.com/dracor-org/dracor-textbook/blob/main/docs/chapters/04-front-end-navigating-dracor) in the learning session.

## 8. Further Reading and Resources

Readers interested in general approaches to corpus building may read {cite:t} `schoech2017aufbau` as a beginner-friendly introduction. Those who would like to delve into “digital corpus archaeology”, i.e. investigating the history of a digital corpus, may consult {cite:t}`borner2024cls`.

## 9. Glossary Entries

| Term | Definition[^cb-definition-info] |
| --- | --- |
| Corpus | A corpus is a text collection selected based on specific criteria. |

| (to) encode / Encoding | In the context of TEI/XML, the verb “encode” refers to the process of adding information to an electronic text, e.g. in the form of XML tags. The noun “encoding” refers to the result of this procedure, e.g. the XML markup in a file. |
| HTML | An abbreviation for the “**H**yper**t**ext **Markup** **L**anguage” commonly used on websites. |
| HTR | An abbreviation for “Handwritten Text Recognition” that refers to the process of generating machine-readable text from an image of a manuscript, e.g. from a scan. |
| LLM | An abbreviation for “**L**arge **L**anguage **M**odel”, a type of artificial intelligence that generates text. Large Language Models may serve as the basis of Chatbots. |
| (to) mark up / markup | In the context of TEI/XML, the noun “markup” refers to the information added to an electronic text in the form of XML tags. The verb “mark up” refers to the process of adding this information to the text. |
| OCR | An abbreviation for “Optical Character Recognition” that refers to the process of generating machine-readable text from an image of said text, e.g. from a scan. |
| Python | Python is a programming language. |
| Regular expression | Regular expressions consist of one or more characters or symbols through which a text may be searched for certain patterns. In find-and-replace actions or programming scripts, regular expressions may serve as placeholders to address these patterns to encode them in a certain way in TEI/XML. |
| TEI | An abbreviation for “**T**ext **E**ncoding **I**nitiative” which may refer to that organisation, its encoding guidelines, or files that follow those guidelines. |
| XML | An abbreviation for “e**X**tensible **M**arkup **L**anguage”, a method for marking up texts and encoding information. |
| XQuery | An abbreviation for “**X**ML **Query** Language”, a programming language. |
| XSLT | An abbreviation for “E**X**tensible **S**tylesheet **L**anguage **T**ransformations”, a programming language. |

## 10. Next Steps
Continue with chapter 2, “TEI Encoding: Preparing Texts for Programmable Corpora”, to learn how the dramatic texts are encoded in DraCor.

## 11. AI Use Declaration
In chapters 4 and 5, Daniil Skorinkin used Claude Opus 4.6 in the process of literature review – literature search and systematisation, writing and editing – text generation, and writing and editing – formulation of conclusions. In the other chapters, no generative AI was used.

## 12. Author Contributions
Daniil Skorinkin – investigation, writing – original draft 
Julia Jennifer Beine – conceptualisation, writing – original draft, writing – review & editing

## 13. References

```{bibliography}
:filter: docname in docnames
```

## 14. Footnotes
[^information]: The following paragraphs on the genesis of GerDraCor are closely based on the CLS INFRA D7.3 report {cite:p}`borner2024cls`, with the permission of the authors.  
[^play-number]: Source distribution retrieved from the [DraCor API](https://dracor.org/api), 2 March 2026.  
[^cb-definition-info]: For this glossary, we consulted the Oxford English Dictionary {cite:p}`oxfordenglishdictionary2023markup, oxfordenglishdictionary2025encode, oxfordenglishdictionary2025regular`. 