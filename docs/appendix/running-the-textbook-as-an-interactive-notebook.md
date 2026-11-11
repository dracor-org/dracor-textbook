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

Both services build the same environment from the [textbook repository](https://github.com/dracor-org/dracor-textbook) and open the page in JupyterLab. You can also set up this environment on your own computer (see A.7).

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

```{figure} ../images/appendix/eu-node-overview.png
:name: fig-eu-node-overview
:alt: The overview page of the EOSC EU Node with the access group in the top right corner and tiles for the services.

The overview of an EOSC EU Node account. The access group is shown in the top right corner (here *Investigator (AP-B)*); the tiles show which services you can use. Personal details have been removed.
```
3. The access group decides what you may use. It is derived from the affiliation your institution sends during login (for example faculty, staff or student). According to the [EU Node User Access Policy](https://open-science-cloud.ec.europa.eu/about/access-policy) (version 2.6), Interactive Notebooks and Binder are available to the groups *Collaborator* and *Investigator*. In other groups you can look around, but you cannot start services.
4. If your access group does not match your role, contact the IT department of your institution, which controls the affiliation that is sent, and the [EU Node helpdesk](https://open-science-cloud.ec.europa.eu/support/helpdesk). Sorting this out can take a while; the blog post [*The Cloud, the Credits and a Coding Agent*](https://blog.dracor.org/posts/cloud-credits-coding-agent-own-dracor-eosc-eu-node/) tells one such story.

Logging in and checking your access group costs nothing.

## A.3. Activating Interactive Notebooks

Binder on the EU Node is part of the **Interactive Notebooks** service, which has to be activated once:

1. In the menu on the left, under *Services*, choose **Interactive Notebooks**.
2. Under *Available EOSC EU Node servers*, request the **Small** server with **Get access**. Once it is active, its button changes to **Start**.
3. The box **EOSC EU Node Binder** is now available. **View externally** opens the Binder start page.
4. Note the **cluster** of your server, shown as a label (**EU-1** or **EU-2**). The EU Node runs on two clusters, and you are not always assigned the same one. The rocket button of the textbook uses the Binder on EU-2; if your server is on EU-1, see A.9.

```{figure} ../images/appendix/eu-node-interactive-notebooks.png
:name: fig-eu-node-interactive-notebooks
:alt: The Interactive Notebooks page of the EOSC EU Node with the server sizes Small, Medium and Large and the box EOSC EU Node Binder.

The Interactive Notebooks page of the EOSC EU Node (open-science-cloud.ec.europa.eu/dashboard/notebooks). The Small server is active (*Start*); the box *EOSC EU Node Binder* links to the Binder service. Personal details have been removed.
```

## A.4. Launching a Page

1. Open the chapter or self-test in the textbook, click the rocket icon and choose **EOSC EU Node** (or **mybinder.org**).
2. Log in if you are asked to. Binder then builds the environment. The first build takes several minutes; later launches are faster.

```{figure} ../images/appendix/eu-node-binder-build.png
:name: fig-eu-node-binder-build
:alt: The EU Node Binder page while launching, with a progress bar showing the stages Waiting, Building, Pushing and Launching.

Binder builds the environment and launches the server. The progress bar shows the stages; *Build Logs* shows the details.
```
3. JupyterLab opens the page as a notebook. If it is shown as a text file instead, right-click the file in the file browser on the left and choose **Open With → Notebook**. If JupyterLab opens in the top folder of the repository instead (for example after launching without a file, see A.9), double-click the folder `docs`, then `chapters` for the chapters or `assessment` for the self-tests.

```{figure} ../images/appendix/jupyterlab-open-with-notebook.png
:name: fig-jupyterlab-open-with-notebook
:alt: JupyterLab with the context menu of the chapter file and the submenu Open With, Notebook.

If the page is shown as a text file: right-click the file in JupyterLab and choose *Open With → Notebook*.
```
4. Run the cells one after another with *Shift + Enter*.

Your changes are not saved back to the textbook. To keep your notebook, download it with *File → Download*.

## A.5. Stopping the Server

The server contains the whole textbook. To work on another chapter or self-test, open it from the file browser of the running JupyterLab (in the folders `docs/chapters` and `docs/assessment`); you can have several open at the same time.

On the EOSC EU Node you can run only one notebook server at a time. Before you launch notebooks from another repository or project, stop the running server: choose *File → Hub Control Panel* in JupyterLab, or open the [Hub Control Panel](https://binder.eu-2.notebooks.open-science-cloud.ec.europa.eu/hub/hub/home) directly, and click **Stop My Server**. Otherwise, a server stops by itself after one hour of inactivity.

```{figure} ../images/appendix/jupyterlab-hub-control-panel-menu.png
:name: fig-jupyterlab-hub-control-panel-menu
:alt: The File menu of JupyterLab with the entry Hub Control Panel.

*File → Hub Control Panel* in JupyterLab.
```

```{figure} ../images/appendix/eu-node-hub-control-panel.png
:name: fig-eu-node-hub-control-panel
:alt: The Hub Control Panel of the EU Node Binder with the buttons Stop My Server and My Server.

The Hub Control Panel of the EU Node Binder. *Stop My Server* stops the running server.
```

A Small server uses 0.04 credits per hour. Credits are virtual and have no monetary value: every account with access to the services receives an allocation free of charge (1,000 credits for *Collaborators*, 2,000 for *Investigators*), which is reset every 90 days. An hour of notebook work therefore uses only a tiny fraction of your allocation.

## A.6. Using mybinder.org

On mybinder.org no account is needed: choose **mybinder.org** in the rocket menu, wait for the build and continue as in A.4. Its resources are shared by all users, so a launch may take longer or fail when the service is busy; in that case, try again later. A session ends after a short period of inactivity, and nothing is stored, so download your notebook if you want to keep it.

## A.7. Running the Textbook on Your Own Computer

You can also run the textbook on your own computer, in the same environment as on the EOSC EU Node and mybinder.org. You need [Python](https://www.python.org/) (version 3.11 or newer), [Git](https://git-scm.com/) and internet access, since the code cells call the DraCor API on dracor.org.

1. Get a copy of the textbook repository:

   ```bash
   git clone https://github.com/dracor-org/dracor-textbook.git
   cd dracor-textbook
   ```

2. Create a virtual environment and install the packages listed for Binder:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   pip install -r .binder/requirements.txt
   ```

3. Optionally, make JupyterLab open the pages as notebooks by default (macOS and Linux):

   ```bash
   bash .binder/postBuild
   ```

   Otherwise, right-click a page in JupyterLab and choose **Open With → Jupytext Notebook**.

4. Start JupyterLab, which opens in your browser:

   ```bash
   jupyter lab
   ```

   The chapters are in the folder `docs/chapters`, the self-tests in `docs/assessment`.

To stop JupyterLab, press *Ctrl + C* in the terminal. To work with a DraCor instance on your own computer instead of dracor.org, see Chapter 6.

## A.8. Why Not Google Colab?

[Google Colab](https://colab.research.google.com/) is a popular service for running Jupyter notebooks in the browser. The rocket menu does not offer it, for two reasons:

- **Colab can only open notebooks in the `.ipynb` format**, from GitHub, Google Drive or a GitHub Gist. The pages of this textbook are written in MyST Markdown (`.md`) and only converted into notebooks when the book is built. A link that opens a page of the textbook directly in Colab is therefore not possible.
- **Colab does not include all packages the textbook needs**, in particular PyDraCor, and the self-tests additionally depend on a helper file of the textbook repository. On the EOSC EU Node and on mybinder.org, these are installed automatically from the repository.

In addition, Colab requires a Google account and is not part of the European Open Science Cloud.

If you nevertheless want to use Colab for chapter 5, you can do so by hand: download the chapter as a notebook with the download button at the top of the page (*.ipynb*), upload it in Colab (*File → Upload notebook*), and add a cell at the beginning with `%pip install pydracor`. The self-tests cannot be run in Colab this way.

## A.9. Troubleshooting

**The rocket button does not work, or your server is on EU-1.** The button links to the Binder on the EU-2 cluster. Instead, open the Binder that belongs to your account: on the Interactive Notebooks page, click **View externally** in the box *EOSC EU Node Binder* and enter

- repository: `dracor-org/dracor-textbook`
- branch: `main`
- path to a file, for example: `docs/chapters/05-api-working-with-dracor-programmatically.md`


```{figure} ../images/appendix/eu-node-binder-form.png
:name: fig-eu-node-binder-form
:alt: The start page of the EU Node Binder with the form Build and launch a repository, filled in with dracor-org/dracor-textbook.

The start page of the EU Node Binder, reached via *View externally*. Enter the repository, the branch (*Git ref*) and the file to open, then click *launch*.
```

Then launch and continue with step 3 in A.4.

**"You already have a running server".** Stop the running server first (see A.5) and launch again.

**The launch still fails.** Contact the [EU Node helpdesk](https://open-science-cloud.ec.europa.eu/support/helpdesk), or use mybinder.org in the meantime (A.6).

## AI Use Declaration

This appendix was drafted with a coding agent (Claude Code, Anthropic), based on the author's notes, a test launch on the EOSC EU Node and the EU Node User Access Policy (version 2.6). Each change was approved by the author.
