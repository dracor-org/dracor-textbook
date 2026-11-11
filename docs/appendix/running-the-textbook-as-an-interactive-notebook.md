---
title: "Running the Textbook as an Interactive Notebook"
author: "Ingo Börner"
date: "2026-11-11"
description: "How to run the Python code of the DraCor Textbook on the EOSC EU Node Binder or on mybinder.org, without installing anything."
keywords: ["DraCor", "Binder", "Jupyter", "EOSC EU Node", "mybinder.org", "Interactive Notebooks"]
license: "CC BY 4.0"
---

# Appendix A: Running the Textbook as an Interactive Notebook

```{admonition} Appendix metadata
:class: tip

**Author:** Ingo Börner  
**Version:** 0.1 (2026-11-11)  
```

Chapter 5 and the self-tests of the DraCor Textbook contain Python code that you can run yourself. You can copy the code into your own Python environment, or you can open a page as a Jupyter notebook in the browser, without installing anything. Pages with runnable code have a rocket icon at the top. It offers two services:

- **EOSC EU Node**: the Binder service of the [EOSC EU Node](https://open-science-cloud.ec.europa.eu/), of the European Open Science Cloud. It requires an institutional login.
- **mybinder.org**: the free public [Binder](https://mybinder.org/) service. It requires no login.

Both services build the same environment from the [textbook repository](https://github.com/dracor-org/dracor-textbook) and open the page in JupyterLab.

## A.1. Which Option to Choose

|  | EOSC EU Node | mybinder.org |
|---|---|---|
| Login | institutional account | none |
| Who can use it | depends on your access group (see A.2) | everyone |
| Resources | guaranteed capacity (Small: 2 vCPUs, 4 GB RAM) | shared; can be slow or temporarily unavailable |
| Cost | free; uses the virtual credits of your EU Node account (no real money, see A.5) | free |

If you have access to the EOSC EU Node, use it. Otherwise, mybinder.org is the quickest way to try the code.

## A.2. Getting Access to the EOSC EU Node

1. Go to <https://open-science-cloud.ec.europa.eu/> and log in with your university account. The login runs through MyAccessID, which forwards you to the login page of your institution.
2. After logging in, your name and your **access group** appear in the top right corner, for example "Investigator (AP-B)".
3. The access group decides what you may use. It is derived from the affiliation your institution sends during login (for example faculty, staff or student). According to the [EU Node User Access Policy](https://open-science-cloud.ec.europa.eu/about/access-policy) (version 2.6), Interactive Notebooks and Binder are available to the groups *Collaborator* and *Investigator*. In other groups you can look around, but you cannot start services.
4. If your access group does not match your role, contact the IT department of your institution, which controls the affiliation that is sent, and the [EU Node helpdesk](https://open-science-cloud.ec.europa.eu/support/helpdesk). Sorting this out can take a while; the blog post [*The Cloud, the Credits and a Coding Agent*](https://blog.dracor.org/posts/cloud-credits-coding-agent-own-dracor-eosc-eu-node/) tells one such story.

Logging in and checking your access group costs nothing.

## A.3. Activating Interactive Notebooks

Binder on the EU Node is part of the **Interactive Notebooks** service, which has to be activated once:

1. In the menu on the left, under *Services*, choose **Interactive Notebooks**.
2. Under *Available EOSC EU Node servers*, request the **Small** server with **Get access**. Once it is active, its button changes to **Start**.
3. The box **EOSC EU Node Binder** is now available. **View externally** opens the Binder start page.

```{figure} ../images/appendix/eu-node-interactive-notebooks.png
:name: fig-eu-node-interactive-notebooks
:alt: The Interactive Notebooks page of the EOSC EU Node with the server sizes Small, Medium and Large and the box EOSC EU Node Binder.

The Interactive Notebooks page of the EOSC EU Node (open-science-cloud.ec.europa.eu/dashboard/notebooks). The Small server is active (*Start*); the box *EOSC EU Node Binder* links to the Binder service. Personal details have been removed.
```

## A.4. Launching a Page

1. Open the chapter or self-test in the textbook, click the rocket icon and choose **EOSC EU Node** (or **mybinder.org**).
2. Log in if you are asked to. Binder then builds the environment. The first build takes several minutes; later launches are faster.
3. JupyterLab opens and shows the page as a text file. In the file browser on the left, right-click the file and choose **Open With → Notebook**.
4. Run the cells one after another with *Shift + Enter*.

Your changes are not saved back to the textbook. To keep your notebook, download it with *File → Download*.

## A.5. Stopping the Server

On the EOSC EU Node you can run only one notebook server at a time. A server stops by itself after one hour of inactivity. To stop it earlier, for example before launching another page, choose *File → Hub Control Panel* in JupyterLab and click **Stop My Server**.

A Small server uses 0.04 credits per hour. Credits are virtual and have no monetary value: every account with access to the services receives an allocation free of charge (1,000 credits for *Collaborators*, 2,000 for *Investigators*), which is reset every 90 days. An hour of notebook work therefore uses only a tiny fraction of your allocation.

## A.6. Using mybinder.org

On mybinder.org no account is needed: choose **mybinder.org** in the rocket menu, wait for the build and continue as in A.4. Its resources are shared by all users, so a launch may take longer or fail when the service is busy; in that case, try again later. A session ends after a short period of inactivity, and nothing is stored, so download your notebook if you want to keep it.

## AI Use Declaration

This appendix was drafted with a coding agent (Claude Code, Anthropic), based on the author's notes, a test launch on the EOSC EU Node and the EU Node User Access Policy (version 2.6). Each change was approved by the author.
