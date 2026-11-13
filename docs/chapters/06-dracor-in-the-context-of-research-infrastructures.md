---
title: "DraCor in the Context of Research Infrastructures"
myst:
  substitutions:
    chap_title: "DraCor in the Context of Research Infrastructures"
author: "Ingo Börner"
date: "2026-09-14"
description: "This chapter explores DraCor as a research infrastructure: its components, its community and its place in the European Digital Humanities landscape. We then set up a local DraCor instance using Docker, load a corpus and connect it to the tools we learned in previous chapters."
keywords: ["DraCor", "Docker", "infrastructure", "reproducibility", "eXist-db", "XQuery", "containers", "tactical infrastructure", "CLS INFRA"]
license: "CC BY 4.0"
---


# DraCor in the Context of Research Infrastructures

```{admonition} Chapter metadata
:class: tip

**Author:** Ingo Börner  
**Version:** 0.3 (2026-11-10)  
**Review status:** Revised  
**Reviewer:** Antonio Rojas Castro  
```

## 1. Overview

In the previous chapters we used DraCor through its front-end ([chapter 4, “Front-end: Navigating DraCor”](04-front-end-navigating-dracor)) and its API ([chapter 5, “API: Working with DraCor Programmatically”](05-api-working-with-dracor-programmatically)). We learned to browse corpora, retrieve data, and analyse plays programmatically. But we treated DraCor as a given – a service available at dracor.org that simply works. In this chapter, we open the box.

What is DraCor, technically? Not a single application, but a system – a set of interconnected services, maintained by a community, funded by research projects, and embedded in a broader European infrastructure landscape. Understanding this matters for at least three reasons. First, it builds **trust**: if we base our research on a system, we should understand what it is and who keeps it running. Second, it enables **adaptation**: knowing the components means we can run DraCor locally, load our own corpora, and tailor it to our research needs. Third, it fosters **critical awareness**: the data and metrics we retrieve through the API are not simply “there” – they are produced by specific software components, from specific encodings, through specific processes. Understanding this makes us better researchers.

The first part of the chapter is conceptual; the second part is practical: we set up a local DraCor instance with Docker, load a corpus, and connect it to the API skills from [chapter 5](05-api-working-with-dracor-programmatically).

## 2. Requirements and Competences

* Familiarity with the DraCor front-end ([chapter 4](04-front-end-navigating-dracor)) and the API ([chapter 5](05-api-working-with-dracor-programmatically)).
* For the practical sections: [Docker](https://www.docker.com/) installed on your machine.
* No programming required for the conceptual sections.

## 3. Learning Outcomes

After completing this chapter, learners will be able to:

1. Explain what a research infrastructure is and why it matters for Computational Literary Studies.
2. Describe the main components of the DraCor system and how they interact.
3. Identify the human actors and community structures that sustain DraCor.
4. Explain why running DraCor locally is useful for research and reproducibility.
5. Set up a local DraCor instance using Docker.
6. Load a corpus into a local DraCor instance and use it with the API.

## 4. Theoretical Background

### 4.1. What Is a Research Infrastructure?

The term “infrastructure” often evokes images of large-scale systems – servers, data centres, networks. But in the humanities, infrastructure is something both more modest and more interesting. In this chapter, when we speak of **research infrastructure**, we mean primarily the technical systems – the software components, services, and data stores – that make a platform like DraCor work. But we will also see that infrastructure cannot be separated from the people who build and maintain it: the developers, editors, and community of contributors without whom the technical system would quickly become unusable.

We tend not to think about infrastructure when it works – we simply use the front-end, call the API, download a file. It becomes visible when something breaks, when we need to understand where a value comes from, or when we want to adapt the system for our own purposes. This chapter is about making the infrastructure visible – not because it is broken, but because understanding it makes us better users and more critical researchers.

A small example: DraCor has no search function. We cannot type a keyword and find all plays that mention “revolution” or all characters named “Maria.” For anyone used to modern web applications, this feels like a missing feature – and it is. But it is also a window into the infrastructure. The core of DraCor is an XML database (eXist-db) with an API designed around the two entities **corpus** and **play**. Full-text search was never built into this design; what was built in is the ability to extract and serve specific **layers** of a text – spoken text, stage directions, network data. This is a deliberate architectural choice, shaped by the research questions that drove the development of DraCor. DraCor grew out of the [DLINA project](https://dlina.github.io/) (Digital Literary Network Analysis), a research initiative by Peer Trilcke and Frank Fischer that focused on extracting and analysing co-presence networks from dramatic texts. In DLINA, there were no full texts – only structural data derived from TEI-encoded plays: acts, scenes, and which characters appear together. Network metrics were calculated from this structural information using tools like dramavis. When DLINA evolved into DraCor, the full TEI-encoded texts were included, but the infrastructure retained its focus on structure – segments, characters, networks, metrics – rather than on full-text search. Understanding infrastructure means understanding choices like these – and, perhaps, contributing to changing them.

On the European level, significant investment goes into building research infrastructures for the humanities. Two major initiatives are [CLARIN](https://www.clarin.eu/), which provides language resources and technology, and [DARIAH](https://www.dariah.eu/), which supports digital research practices in the arts and humanities more broadly. Both are organised as European Research Infrastructure Consortia (ERICs) – long-term, internationally funded organisations that aim to provide sustainable, shared infrastructure across national boundaries. Together with other ERICs, they form the Science Cluster for the Social Sciences and the Humanities ([SSHOC](https://sshopencloud.eu/)). Resources from this broader landscape are directly relevant to working with DraCor: [DARIAH Campus](https://campus.dariah.eu/) provides training materials, the [CLARIN Language Resource Switchboard](https://switchboard.clarin.eu/) allows users to chain tools for working with textual data – and is directly accessible from the Tools tab of DraCor (see [chapter 4](04-front-end-navigating-dracor); {cite:alp}`borner2025cls`) – and the [SSH Open Marketplace](https://marketplace.sshopencloud.eu/) catalogues tools and workflows for the humanities. 

The approach of DraCor to infrastructure is different. Rather than building a large-scale centralised platform, it grew from the bottom up – from a specific research need (network analysis of drama) to a multi-component system serving a growing community. This trajectory reflects what Tim Sherratt called “tactical infrastructure” in [“Towards a Manifesto for Tactical DH Research Infrastructure”](https://www.youtube.com/watch?v=FL5pP2ysjU4):

> “The perception of infrastructure as a series of big machines really obscures the emergence of ... a bottom-up infrastructure ... the tools, the methodologies, the expertise, a network of people, data and code.”

The [CLS INFRA project](https://clsinfra.io) adopted this concept of tactical infrastructures as the foundation of its approach to building infrastructure for Computational Literary Studies. Rather than creating a single centralised platform, the project aimed for “a tactical infrastructure as an ecosystem of API-enabled ‘Programmable Corpora’” – distributed, open, and built around the actual practices of researchers {cite:p}`borner2023cls`. DraCor is the prototype that realises this vision.

CLS INFRA identified three core challenges facing the resources of the field: **dispersion** (data scattered across projects and platforms), **heterogeneity** (different formats, standards, and conventions), and **instability** (for example, corpora that change over time). The infrastructural responses to these challenges – a distributed architecture, workflows for homogenisation, and versioning techniques – are embodied in the design of DraCor {cite:p}`borner2023cls`. And our missing search function? It is a reminder that tactical infrastructure serves the needs it grew from – network analysis, structural analysis – and has not yet grown to serve all needs equally. That is neither a failure nor permanent; it is simply where the infrastructure is today – and an invitation. In an open-source, community-driven project like DraCor, the absence of a feature is not a closed door but an open one: if the community identifies a need, it can propose, discuss, and contribute to implementing it. This points to another dimension of infrastructure that goes beyond technology and community: **governance** – the question of how decisions about the future direction of the infrastructure are made, who sets priorities, and how the needs of a diverse user base are balanced against the resources available for development.

### 4.2. DraCor as a System: The Components

Whether we want to work **with** DraCor – using it for our research – or work **on** DraCor – contributing to its development, adapting it for new corpora or new research questions – it helps to understand how the system works on the inside. DraCor is not a single application but a multi-component system. For a detailed technical description of all components, see {cite:t}`borner2023cls`. The following diagram, adapted from {cite:t}`borner2023cls`, shows how the components fit together:

```{figure} ../images/infrastructure/dracor-infrastructure-drawing.png
---
alt: "Diagram of the DraCor system architecture showing corpus repositories, eXist-db with the API and storage, the Metrics Service, the front-end and the Triple Store."
width: 100%
---
Overview of the DraCor system. Corpus data flows from GitHub repositories into the eXist-db database, where the API provides access. The Metrics Service computes network metrics and the Triple Store holds RDF representations accessible via SPARQL.
```

Let us walk through the main components:

**Corpus repositories on GitHub.** The source data – TEI-encoded play documents and corpus metadata – is curated in GitHub repositories under the [dracor-org](https://github.com/dracor-org) organisation. Each corpus (GerDraCor, RusDraCor, etc.) has its own repository. GitHub provides version control via Git, issue tracking for community discussions, and a transparent development history. This is also where corpus contributors submit new plays or corrections via pull requests. It is worth noting a tension here: DraCor is committed to open science and open source, yet it relies on GitHub – a commercial platform owned by Microsoft – for hosting its code and data. This is a pragmatic choice (GitHub is where the community still is, and its features for collaboration are hard to match), but it means that a core part of the infrastructure depends on a proprietary service. This is not unique to DraCor; it is a widespread dependency in open-source projects and in Digital Humanities more broadly, and one that the community should remain aware of.

**eXist-db and the DraCor API.** At the core of the system sits [eXist-db](http://exist-db.org), an open-source XML database widely used in Digital Humanities. The DraCor API is implemented as an eXist-db application ([GitHub repository](https://github.com/dracor-org/dracor-api)), written in [XQuery](https://www.w3.org/TR/xquery/) using the RESTXQ framework. XQuery is a query language designed for XML data – it is the natural choice for working with TEI-encoded texts, though it is uncommon outside the humanities and XML communities. When corpora are loaded into eXist-db, the extraction and processing logic of the API parses the TEI documents, extracts metadata, character information, spoken text, stage directions, and other layers, and makes them available through the endpoints we explored in [chapter 5](05-api-working-with-dracor-programmatically).

```{admonition} The X technology stack
:class: note
DraCor is built on what is sometimes called the “X technology stack” – a set of XML-based technologies common in Digital Humanities: XML as the data format, TEI as the encoding standard, XSLT for transformations, XQuery for database queries and API logic, RELAX NG for schema validation, and ODD for documenting TEI customisations (see [chapter 3, “TEI Encoding: Preparing Texts for Programmable Corpora”](03-tei-encoding-preparing-texts-for-programmable-corpora)). While this stack is less common in mainstream software development, it is well-suited for working with richly structured textual data in the humanities.
```

**The Metrics Service.** Network metrics (density, diameter, average path length, etc.) are not computed by the eXist-db application itself but by a separate service – the Metrics Service, written in Python ([GitHub repository](https://github.com/dracor-org/dracor-metrics)). During the ingest of a play, the API extracts the co-presence network from the TEI structure and sends it to the Metrics Service, which calculates the network metrics and returns them. These pre-calculated metrics are then stored in the XML database. This is an example of a **microservice** architecture: rather than one monolithic application doing everything, specialised services handle specific tasks and communicate via APIs.

**The front-end.** The web interface at dracor.org is a React application – a JavaScript-based single-page application that communicates with the DraCor API. As we learned in [chapter 5](05-api-working-with-dracor-programmatically), the front-end is itself an API client: every page, every tab, every download button sends requests to the API and displays the results. The front-end code is maintained in its own [GitHub repository](https://github.com/dracor-org/dracor-frontend).

**The Triple Store.** DraCor also generates RDF (Resource Description Framework) representations of plays and their metadata, which are stored in a Triple Store (Apache Jena Fuseki). This provides a SPARQL endpoint for linked data queries – connecting DraCor data to the broader Linked Open Data cloud, including Wikidata. We do not cover SPARQL in this textbook – the linked data layer is currently the least developed part of the DraCor system and still evolving. But it is worth knowing that this component exists and points toward a future in which DraCor data can be queried in relation to external knowledge bases.

**Reuse of the technology stack.** The DraCor system is not limited to drama. The same technology stack has been adapted for other domains: [EcoCor](https://ecocor.org) applies it to texts relevant for ecocriticism, and an [ELTeC corpus explorer](https://eltec.clscor.io) uses it for the European Literary Text Collection (prose). Adapting DraCor for a new domain requires working with the XQuery code – a step beyond what this textbook covers, but one that the open-source nature of the project makes possible.

### 4.3. The Ecosystem: People and Community

Infrastructure is not only technology – it is also the people who build, maintain, and use it. DraCor is maintained by a core team of editors and technical leads, and each corpus has its own editors and contributors – scholars who curate the TEI-encoded plays, often as part of their own research.[^credits]

Infrastructure development in the humanities is inherently interdisciplinary, requiring expertise from humanists, technologists, and data curators alike. The role of the technical lead – in the case of DraCor, Carsten Milling – deserves particular attention. Without continuous maintenance – updating dependencies, fixing bugs, adapting to new server environments, responding to community needs – the platform would quickly become unusable. This kind of work is often invisible but essential.

DraCor is explicitly an open-source project – everybody is welcome to contribute. Community interaction happens through several channels: GitHub (for issues, pull requests, and technical discussions), a Mattermost server hosted by the University of Potsdam (for informal communication), social media (primarily Bluesky), and an email list. This community dimension is not incidental; it is what allows the corpora to grow organically, following the “natural growth” principle that Aaron Swartz described and that the Programmable Corpora concept embraces {cite:p}`borner2023cls`.

## 5. Practical Examples: Running DraCor Locally

In the previous sections we looked at DraCor from the outside – its components, its community, its place in the European infrastructure landscape. Now we turn to practice. Because DraCor is open source and its services are published as Docker images, we are not limited to using the production instance at dracor.org. We can run the entire system on our own machine – the same API, the same front-end, the same metrics service – and use it for our own purposes: testing a corpus we are building, working with custom data, or simply exploring how the system works from the inside.

```{admonition} Technical note
:class: warning
The following sections involve working with the **terminal** (also called command line or shell) – a text-based interface for running commands on your computer. On macOS, this is the Terminal application; on Linux, a terminal emulator; on Windows, [PowerShell](https://learn.microsoft.com/en-us/powershell/) or the Command Prompt. Some commands shown here (particularly `curl`) may behave slightly differently on Windows. If you are on Windows and encounter issues, using the terminal inside [WSL 2 (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) – which you will need for Docker anyway – is recommended.[^dind]
```

### 5.1. Why Run DraCor Locally?

There are several practical reasons to set up a local DraCor instance:

- **Independence.** A local instance does not depend on the dracor.org server being available – although its uptime is generally good. Once the Docker images and the corpus data have been downloaded, you can work offline, without being affected by changes to the production system.
- **Testing your own corpus.** If you are developing a new corpus of TEI-encoded plays (see [chapter 3](03-tei-encoding-preparing-texts-for-programmable-corpora)), you can load it into a local DraCor to see how it looks in the front-end and how the API processes it – before contributing it to the community.
- **Working with custom data.** You may want to work with plays that are not (yet) on dracor.org, or with a specific subset of plays for a particular research question.
- **Controlling the data version.** DraCor corpora are “living corpora” – they change over time as plays are added, corrected, or re-encoded {cite:p}`borner2024cls`. The data on dracor.org can change without further notice – corpora are updated, plays added or corrected – and as a user, you do not know when this happens. A local instance lets you work with a specific, known version of the data.
- **Reproducibility.** If we want to ensure that our research can be reproduced, we need a way to freeze the state of both the data and the software at a specific point in time. As Andrew Piper noted about his own computational analyses in the foreword to his book “Enumerations” addressing the reproducibility challenges, code “works, at least as of today” {cite:p}`borner2023dockerizing` – but “today” passes. A local DraCor instance, captured as a Docker image, preserves both the data and the infrastructure together, so that the same analysis can be re-run under the same conditions – as demonstrated in {cite:t}`trilcke2024detecting`, where a Dockerised DraCor environment was used to ensure the reproducibility of a network-analytic study across thousands of plays in a custom “Very Big Drama Corpus” (VeBiDraCor).

```{admonition} The reproducibility challenge in CLS
:class: note
The question of reproducibility in Computational Literary Studies has received increasing attention. Nan Z. Da’s critique of CLS in 2019 pointed out cases where results could not be reproduced {cite:p}`da2019computational`. Christof Schöch considers Da’s paper highly problematic, but notes that it points to “serious and relevant challenges for the field of CLS”, above all the difficulty of reproducing work in the field {cite:p}`schoech2023repetitive{p. 379}`. He developed a comprehensive framework for “repetitive research” that distinguishes replication, reproduction, revision, and other forms. The living nature of DraCor corpora adds another dimension: even with the same code, results may change if the underlying data has been updated. For a detailed discussion and practical solutions, see {cite:t}`borner2024cls`.
```

### 5.2. What Is Docker?

We have mentioned Docker several times now – as the technology behind the local deployment of DraCor, and as the mechanism that made the VeBiDraCor study reproducible. But what is it, exactly?

Docker is a tool for creating and running **containers** – lightweight, portable environments that bundle an application together with everything it needs to run: its code, its libraries, its configuration. A container is like a self-contained package: if it runs on one machine, it will run on another, regardless of what operating system or software is installed on the host.

This is different from simply downloading and running code. If we tried to install the components of DraCor manually – eXist-db, the XQuery application, the Python Metrics Service, the React front-end, the Triple Store – we would need to manage numerous dependencies, configure services to communicate with each other, and resolve conflicts with other software on our machine. The XML database eXist-db alone, for example, requires a specific version of Java – and managing Java versions across different applications is a well-known source of frustration. Docker abstracts all of this away: each container carries its own dependencies, so we do not need to install Java, Python, or Node.js on our system.

Two key concepts:

- An **image** is a snapshot of an application and everything it needs – frozen in a file that can be shared and reused. DraCor publishes images for its services on [Docker Hub](https://hub.docker.com/u/dracor): `dracor/api`, `dracor/frontend`, `dracor/metrics`, and `dracor/fuseki`.
- A **container** is what happens when we run an image – a live, working copy of the application. We can start, stop, and inspect containers.

Docker Compose allows us to define and run multiple containers together – think of it as a blueprint that specifies which services to start, how they connect, and in what order. This is exactly what we need for DraCor, since the system consists of several services that need to communicate with each other.

This combination of Docker and Compose is what makes sharing and documenting a DraCor setup so lightweight. Since the images are already published on Docker Hub, all we need to share is the Compose file – a small text file that contains all the information needed to start and orchestrate the services. Anyone with Docker installed can take that file, run `docker compose up`, and have the same system running on their machine. This only works reliably if the Compose file specifies exact image versions (for example `dracor/api:1.4.1` rather than `dracor/api:latest`); otherwise, `docker compose up` downloads whatever version is current at the time, and the result may differ from the original setup. This also means that any adaptations we make to our local setup – adding a service, changing a configuration – are documented in the Compose file itself rather than in our memory.

```{admonition} A transferable skill
:class: tip
Containerisation is not unique to DraCor or to Digital Humanities. It is a core practice in modern software development and “DevOps” – the discipline of managing the deployment and operation of applications {cite:p}`borner2024cls`. Understanding Docker here means recognising the same patterns when encountering them in industry contexts or other research infrastructure.
```

### 5.3. Setting Up a Local DraCor Instance

The [DraCor API repository on GitHub](https://github.com/dracor-org/dracor-api) contains everything we need to run DraCor locally.[^docker-notebook] The following steps assume that Docker is installed and running on your machine. On macOS and Linux, installation is usually straightforward. On Windows, Docker requires the Windows Subsystem for Linux (WSL 2) to be enabled, which can be an additional hurdle – consult the [Docker documentation](https://docs.docker.com/desktop/install/windows-install/) if you encounter issues.

**Step 1: Clone the repository.**

We need a local copy of the DraCor API code. For this, we use [Git](https://git-scm.com/) – a version control system that tracks changes to files over time. Git is widely used in software development and in Digital Humanities for managing both code and data (the corpora of DraCor are also managed with Git). If Git is not yet installed on your system, see the official installation guide.[^git-install] The command `git clone` creates a local copy of a repository on your machine. The `cd` command enters the newly created folder:

```bash
git clone https://github.com/dracor-org/dracor-api.git
cd dracor-api
``` 

**Step 2: Start the services.**

The repository contains a `compose.yml` file that defines all the services DraCor needs. We start them with a single command:

```bash
EXIST_PASSWORD= docker compose up
```

Setting `EXIST_PASSWORD=` (empty) disables the admin password for the local instance, which is convenient for development. The first time you run this, Docker will download the necessary images – this may take a few minutes.

Once the services are running, we can verify that the API is operational. Note that `http://localhost:8088/api/v1/` is now the base URL for our local API – the equivalent of `https://dracor.org/api/v1/` that we used throughout [chapter 5](05-api-working-with-dracor-programmatically). Everything we learned there – calling endpoints with `curl`, Python `requests`, or PyDraCor – works the same way with this local URL:

```bash
curl http://localhost:8088/api/v1/info
```

The front-end is now available at [http://localhost:8088](http://localhost:8088). It is the same software as on dracor.org, although the `compose.yml` in the repository may refer to newer versions than those currently running on dracor.org. It runs entirely on your machine, and it is empty: no corpora are loaded yet.

### 5.4. Loading a Corpus

An empty DraCor is not very useful. Let us load a corpus. The DraCor API provides admin endpoints for this purpose – the same endpoints we briefly mentioned in [chapter 5](05-api-working-with-dracor-programmatically) but did not use, because they require authentication. On the production server, only the administrators have these credentials. On our local instance, however, we set the password ourselves (or left it empty), so we can use these admin endpoints to manage our local DraCor.

Adding a corpus is a two-step process: first, we **register** the corpus by sending its metadata to the API; then, we **trigger the loading** of the actual play data. Let us walk through both steps.

**Step 1: Register the corpus.**

We first register a new corpus by sending its metadata (as an XML document) to the API. Each DraCor corpus repository on GitHub contains a `corpus.xml` file with this metadata. We can download it directly using the raw file URL that GitHub provides – a URL that serves the plain file content rather than the GitHub web page. For example, to add TestDraCor, a small corpus for testing purposes:

```bash
curl https://raw.githubusercontent.com/dracor-org/testdracor/main/corpus.xml | \
curl -X POST -u admin: -d@- -H 'Content-type: text/xml' \
http://localhost:8088/api/v1/corpora
```

The first `curl` downloads the corpus metadata from GitHub; the pipe (`|`) passes it to the second `curl`, which sends it to our local API. Note the new flags: `-X POST` tells `curl` to use the POST method instead of GET – because we are **creating** a new resource, not just retrieving data (recall the HTTP methods we introduced in [chapter 5](05-api-working-with-dracor-programmatically)). `-u admin:` provides the admin credentials (username “admin”, empty password). `-d@-` reads the data from the pipe. `-H 'Content-type: text/xml'` tells the API that we are sending XML data. This is similar to the content negotiation we discussed in [chapter 5](05-api-working-with-dracor-programmatically), but here we specify the format of what we **send**, not what we want to **receive**.

**Step 2: Trigger loading.**

Next, we tell the API to load the play data from the GitHub repository of the corpus:

```bash
curl -X POST -u admin: -H 'Content-type: application/json' \
-d '{"load":true}' http://localhost:8088/api/v1/corpora/test
```

Once the loading is complete, we can check that the plays are available by querying the API:

```bash
curl http://localhost:8088/api/v1/corpora/test | jq
```

Here, `jq` is an optional command-line tool that formats JSON output for readability. If it is not installed, `curl http://localhost:8088/api/v1/corpora/test` works just as well – the output will simply not be indented. Alternatively, we can paste the URL directly into a browser to see the response.

If we refresh the front-end at [http://localhost:8088](http://localhost:8088), we should also see the corpus with its plays – just as we would on dracor.org.

The same two-step process works for any DraCor-compatible corpus hosted on GitHub. To load GerDraCor, for example, we would use its corpus metadata from the [gerdracor repository](https://github.com/dracor-org/gerdracor). We can also load our own TEI files – if we have encoded plays following the DraCor TEI conventions (see [chapter 3](03-tei-encoding-preparing-texts-for-programmable-corpora)), we can upload them through the admin API.

In Python with `requests`, we simply set the base URL to our local instance:

```python
API_URL = "http://localhost:8088/api/v1/"
```

And with PyDraCor:

```python
from pydracor import DraCorAPI
dracor = DraCorAPI(host="http://localhost:8088/api/v1")
```

Everything we learned in [chapter 5](05-api-working-with-dracor-programmatically) – listing corpora, retrieving plays, getting metrics, filtering spoken text – works exactly the same way with the local instance.

### 5.5. Sharing a Research Environment

Once we have a local DraCor instance populated with data, we can go one step further: freezing its state and sharing it. The Docker command `docker commit` creates a new image from a running container – essentially taking a snapshot of the populated database. This image can then be published on Docker Hub, so that other researchers can download it and have the exact same data and infrastructure available on their machine.

Note that `docker commit` captures a single container. For DraCor, this is the `api` container, whose eXist-db database holds the corpus data. The other services – the front-end, the metrics service and the Fuseki triple store – are not part of the snapshot, and Fuseki keeps its data in a separate Docker volume, which `docker commit` never includes. To share the complete environment, we therefore push the committed image to Docker Hub and share a Compose file that refers to it in place of the original `dracor/api` image and specifies the exact versions of all other images. Running `docker compose up` with this file then downloads all images from Docker Hub, including our snapshot.

This is what was done for the “Small Worlds” study {cite:p}`trilcke2024detecting`: the researchers created a “pre-analysis state” image (the populated DraCor with the VeBiDraCor data) and a “post-analysis state” image (the research environment after running the analysis), both published and available for inspection {cite:p}`borner2023dockerizing`. In this way, a Docker image becomes a **research artifact** – a self-contained, shareable package that documents not just the code and data but the entire environment in which the research was conducted {cite:p}`borner2024cls`.

A local instance, however, is yours alone: co-authors, students or reviewers cannot access it. To put your own DraCor online, you can use the Cloud Container Platform of the [EOSC EU Node](https://open-science-cloud.ec.europa.eu/), a node of the European Open Science Cloud (EOSC). Researchers log in with their institutional account and receive credits for computing resources, without an application or a budget; a standard DraCor fits into the smallest container size. The repository [dracor-eosc-eu-node-deploy](https://github.com/dracor-org/dracor-eosc-eu-node-deploy) provides the configuration files, a step-by-step guide, and instructions for a coding agent that guides you through the deployment {cite:p}`borner2026cloud`. Note that loading a corpus this way gives you its current state; such an instance is useful for teaching, demos or sharing a custom corpus, but it does not by itself freeze data and software for reproducibility.

### 5.6. Beyond Using: Adapting DraCor

In this chapter, we loaded existing DraCor corpora into a local instance. But the open-source nature of the system also makes it possible to go further: adapting the DraCor technology stack for entirely different collections of texts. Projects like [EcoCor](https://ecocor.org) (Prose Corpora for Ecocriticism) and the [ELTeC corpus explorer](https://eltec.clscor.io) (European Literary Text Collection Corpora of Novels) have done exactly this – reusing the eXist-db application, API and front-end of DraCor for their own purposes. Adapting DraCor at this level involves working with the XQuery code and the TEI customisation, which is beyond the scope of this textbook. But knowing that it is possible – and that the codebase is open for it – is part of understanding DraCor as infrastructure: not a fixed product, but a platform that can evolve with the needs of the research community.

## 6. Exercises

```{admonition} Self-test
:class: tip
Open the [Self-test: Infrastructure](../assessment/06-dracor-in-the-context-of-research-infrastructures-assessment).
```

## 7. Teaching Notes

This chapter can be taught as a workshop on reproducible research. Its aim is an understanding of what reproducible research with corpora requires: knowing which version of the data and which version of the software were used, and being able to recreate both. The CLS INFRA report on versioning living and programmable corpora {cite:p}`borner2024cls` discusses these questions in more depth.

The chapter offers containers as a practical answer: a Docker image stabilises the software environment, and a corpus loaded at a known state fixes the data. In the author’s experience of teaching this material, the main obstacle is running Docker on the learners’ own computers, especially on Windows. Instructors should plan time for this or use an alternative to local installation.

Such an alternative is the Cloud Container Platform of the EOSC EU Node (section 5.5). Following the separately published guide in the repository [dracor-eosc-eu-node-deploy](https://github.com/dracor-org/dracor-eosc-eu-node-deploy) {cite:p}`borner2026cloud`, a workshop can show how to deploy one’s own DraCor in the cloud, load a custom corpus and share the instance with other participants or colleagues. Note that the EU Node currently requires an institutional account with staff or faculty status; with groups of students, the instructor can carry out the deployment as a demonstration.

## 8. Further Reading and Resources

- DraCor API repository and setup instructions: [https://github.com/dracor-org/dracor-api](https://github.com/dracor-org/dracor-api)
- Reproducible research with Docker notebook: [dracor-notebooks on GitHub](https://github.com/dracor-org/dracor-notebooks/blob/main/reproducible-research-with-docker/reproducible-research-with-docker.ipynb)
- Running your own DraCor on the EOSC EU Node, step-by-step guide: [dracor-eosc-eu-node-deploy on GitHub](https://github.com/dracor-org/dracor-eosc-eu-node-deploy/blob/main/docs/guide-eosc-eu-node.md)
- Börner, I. (2026). “The Cloud, the Credits and a Coding Agent: Your Own DraCor on the EOSC EU Node.” [DraCor Blog](https://blog.dracor.org/posts/cloud-credits-coding-agent-own-dracor-eosc-eu-node/)
- Docker documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Sherratt, T. (2015). “Towards a Manifesto for Tactical DH Research Infrastructure.” [YouTube](https://www.youtube.com/watch?v=FL5pP2ysjU4)
- DARIAH Campus: [https://campus.dariah.eu/](https://campus.dariah.eu/)
- SSH Open Marketplace: [https://marketplace.sshopencloud.eu/](https://marketplace.sshopencloud.eu/)

## 9. Glossary Entries

| Term | Definition |
| --- | --- |
| Container | A running instance of a Docker image – an isolated environment containing an application and everything it needs to run. |
| `curl` | A command-line tool for sending HTTP requests – used in this textbook to interact with the DraCor API. |
| DevOps | A set of practices combining software development and IT operations, often involving containerisation and automated deployment. |
| Docker | A platform for building and running containers – lightweight, portable environments that bundle an application with its dependencies. |
| Docker Compose | A tool for defining and running multi-container applications. DraCor uses it to orchestrate its services. |
| Docker Hub | A cloud-based registry for sharing Docker images. DraCor publishes its service images there. |
| ERIC (European Research Infrastructure Consortium) | A legal framework for establishing and operating European research infrastructures. CLARIN and DARIAH are ERICs. |
| eXist-db | An open-source XML database used as the core of the DraCor system. |
| Git | A distributed version control system that tracks changes to files over time. The corpora and code of DraCor are managed with Git. |
| GitHub | A web-based platform for hosting Git repositories. DraCor uses it for code, corpora, and community collaboration. Owned by Microsoft. |
| Image | A read-only template (blueprint) from which Docker containers are created. DraCor images are published on Docker Hub. |
| Living corpus | A corpus that changes over time – plays are added, corrected, or re-encoded. This creates challenges for reproducibility. |
| Microservice | A small, specialised service that handles a specific task and communicates with other services via APIs. The DraCor Metrics Service is an example. |
| Open source | Software whose source code is publicly available and can be freely used, modified, and distributed. DraCor is an open-source project. |
| RDF (Resource Description Framework) | A standard for representing data as linked triples (subject–predicate–object), used for connecting data to the Linked Open Data cloud. |
| Repository | A project folder managed by Git, containing files and their full change history. |
| Research infrastructure | A system of tools, services, data, and people that supports research activities. In the humanities, often a socio-technical system rather than a purely technical one. |
| SPARQL | A query language for querying RDF (Linked Data). DraCor provides a SPARQL endpoint but this is not covered in this textbook. |
| Tactical infrastructure | An approach to infrastructure that grows bottom-up from researcher needs, rather than being imposed as a centralised platform (term introduced by Sherratt 2015). |
| Terminal (command line) | A text-based interface for running commands on a computer. Called Terminal on macOS, and PowerShell or Command Prompt on Windows. |
| XQuery | A query and programming language for XML databases. The DraCor API is written in XQuery. |

## 10. Next Steps

This chapter concludes the current version of the DraCor Textbook. Readers may continue by experimenting with a local instance: load a small corpus and repeat an API request from [chapter 5](05-api-working-with-dracor-programmatically). To share such an instance with others, they can put their own DraCor online on the EOSC EU Node, as described in section 5.5. Comments, corrections and suggestions for the textbook are welcome in its [GitHub repository](https://github.com/dracor-org/dracor-textbook).

## 11. AI Use Declaration

This chapter was drafted with the assistance of a large language model (Claude, Anthropic). The author dictated content via voice input, which was used as the basis for an interview-style dialogue with the LLM. The model structured and edited the spoken input into chapter prose. A retrieval-augmented generation (RAG) system containing key literature on DraCor and CLS infrastructure was used to retrieve relevant passages and verify factual claims. A summary of the CLS INFRA project proposal and strategic roadmap, generated with the assistance of an LLM, was used as source material. All content was reviewed and edited by the author. The revision for version 0.3 was carried out with a coding agent (Claude Code, Anthropic), which proposed changes, tested the Docker setup and the corpus-loading commands, and checked references against their sources; each change was approved by the author. The Teaching Notes (section 7) and the self-test were written for version 0.3 with the same coding agent (Claude Opus 5.5): the Teaching Notes from the author’s instructions, the self-test questions derived from the chapter; all questions were approved by the author.

## 12. Author Contributions

Ingo Börner – Conceptualisation, Methodology, Software, Writing – original draft, Writing – review and editing.

## 13. References

```{bibliography}
:filter: docname in docnames
```

## 14. Footnotes

[^credits]: For the full list of contributors, see [dracor.org/doc/credits](https://dracor.org/doc/credits). The further development of DraCor is currently supported by the **OSCARS** project (Open Science Clusters’ Action for Research and Society, EU Horizon Europe) through the DraCorOS initiative.

[^dind]: An alternative approach, used at the [ExploreCor training school](https://campus.dariah.eu/resources/events/explore-cor-using-programmable-corpora-in-computational-literary-studies), is to work inside a Docker container that provides a complete Linux environment with JupyterLab – a “Docker in Docker” setup that gives all participants the same working environment regardless of their operating system. See the [dracor-explorecor repository](https://github.com/dracor-org/dracor-explorecor).

[^docker-notebook]: For a more detailed walkthrough, including running Docker from a Jupyter notebook and additional examples, see the [reproducible research notebook](https://github.com/dracor-org/dracor-notebooks/blob/main/reproducible-research-with-docker/reproducible-research-with-docker.ipynb).

[^git-install]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
