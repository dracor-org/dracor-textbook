# DraCor Textbook

The DraCor Textbook is a curated, pedagogically structured Open Educational Resource (OER) developed by the DraCorOS team. It complements (rather than replaces) the community-driven DraCor Notebooks by offering a coherent learning path for working with DraCor’s programmable drama corpora.

The textbook is published as a Jupyter Book website (GitHub Pages) and is under active development.

## Scope and Audience

This textbook is designed for:

- MA students in the humanities with little or no Digital Humanities background
- Library and Information Science students
- Self-study learners and classroom teaching contexts
- Learners with no prior programming experience required (core chapters)

## Repository Structure

The book source lives in `docs/`:

- `docs/` — Jupyter Book source (markdown files / notebooks, `_config.yml`, `_toc.yml`, images, etc.)
- `docs/_static/` — static assets (logo, favicon, etc.)
- `docs/images/` — images used in chapters (recommended: per-chapter subfolders)
- `docs/references.bib` — shared bibliography (BibTeX)
- `binder/` — Binder configuration (optional)

## Build Locally

Prerequisites:

- Python 3.11 (recommended)
- `pip`

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Build the book with: 

```
jupyter-book clean docs --all
jupyter-book build docs --all
```

## Licence

This work is licensed under CC BY 4.0. To view a copy of this licence, visit:
[https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

## Suggested Citation

Rojas Castro, Antonio; Fischer, Frank; Trilcke, Peer; Börner, Ingo; Beine, Julia Jennifer; Skorinkin, Daniil (eds.) 2026. *DraCor Textbook. Book 1*. [https://github.com/dracor-org/dracor-textbook](https://github.com/dracor-org/dracor-textbook). Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

[Author]: [Chapter Title]. In Rojas Castro, Antonio; Fischer, Frank; Trilcke, Peer; Börner, Ingo; Beine, Julia Jennifer; Skorinkin, Daniil (eds.) 2026. *DraCor Textbook. Book 1*. [https://github.com/dracor-org/dracor-textbook](https://github.com/dracor-org/dracor-textbook). Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
