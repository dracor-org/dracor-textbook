#!/usr/bin/env python3
"""Run all executable content of the DraCor Textbook and report errors.

Finds every page under docs/ that is a notebook (MyST Markdown with a
`kernelspec` in its front matter, or .ipynb), executes all code cells from
top to bottom and reports each cell that raises an error. Exits with status 1
if any cell fails.

Usage:
    python scripts/test_executable_content.py            # all pages
    python scripts/test_executable_content.py assessment # only paths containing "assessment"

Requires jupytext, nbclient and ipykernel, plus the packages used in the
pages (see .binder/requirements.txt).
"""

import os
import pathlib
import re
import sys
import time

import jupytext
from nbclient import NotebookClient

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
TIMEOUT = 600  # seconds per cell


def executable_pages(pattern=""):
    for path in sorted(DOCS.rglob("*")):
        if "_build" in path.parts or ".ipynb_checkpoints" in path.parts:
            continue
        if pattern and pattern not in str(path.relative_to(DOCS)):
            continue
        if "template" in path.name:  # placeholders only
            continue
        if path.suffix == ".ipynb":
            yield path
        elif path.suffix == ".md":
            head = path.read_text(encoding="utf-8")[:2000]
            if re.match(r"---\s*\n.*?^kernelspec:", head, re.S | re.M):
                yield path


def run(path):
    notebook = jupytext.read(path)
    client = NotebookClient(
        notebook,
        timeout=TIMEOUT,
        kernel_name="python3",
        allow_errors=True,
        resources={"metadata": {"path": str(path.parent)}},
    )
    client.execute()
    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    errors = []
    for number, cell in enumerate(code_cells, 1):
        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                first_line = cell.source.strip().splitlines()[0] if cell.source.strip() else ""
                errors.append((number, first_line, output["ename"], output["evalue"]))
    return len(code_cells), errors


def main():
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    pages = list(executable_pages(pattern))
    if not pages:
        sys.exit(f"No executable pages found (pattern: {pattern!r}).")

    rows, failed = [], 0
    for path in pages:
        name = path.relative_to(DOCS)
        start = time.time()
        cells, errors = run(path)
        seconds = time.time() - start
        status = "ok" if not errors else f"{len(errors)} error(s)"
        print(f"{name}: {cells} code cells, {status} ({seconds:.0f} s)", flush=True)
        for number, first_line, ename, evalue in errors:
            print(f"  cell {number} ({first_line[:60]}): {ename}: {evalue[:200]}", flush=True)
        failed += bool(errors)
        rows.append((name, cells, status, seconds, errors))

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as out:
            out.write("## Executable content\n\n| Page | Code cells | Result | Time |\n|---|---|---|---|\n")
            for name, cells, status, seconds, _ in rows:
                out.write(f"| `{name}` | {cells} | {status} | {seconds:.0f} s |\n")
            for name, _, _, _, errors in rows:
                for number, first_line, ename, evalue in errors:
                    out.write(f"\n- `{name}`, cell {number} (`{first_line[:60]}`): **{ename}**: {evalue[:200]}")
            out.write("\n")

    print(f"\n{len(pages)} pages, {failed} with errors.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
