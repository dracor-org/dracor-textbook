#!/usr/bin/env python3
"""Document the versions of the DraCor software and corpora.

Writes Markdown tables to stdout:

1. software deployed on a DraCor instance (API, eXist-db, front-end),
2. latest releases of the DraCor software on GitHub (with commit SHAs),
   plus PyPI (pydracor) and CRAN (rdracor),
3. the corpora on the instance: deployed commit, its date and the latest
   commit of the corpus repository.

Usage:
    python scripts/dracor_versions.py [--instance https://dracor.org] > versions.md

GitHub allows 60 unauthenticated requests per hour; the corpus table needs
about 70. Set GITHUB_TOKEN (any token, no scopes needed) to avoid the limit,
e.g. GITHUB_TOKEN=$(gh auth token) python scripts/dracor_versions.py
"""

import argparse
import datetime
import gzip
import json
import os
import re
import sys
import urllib.error
import urllib.request

GITHUB_API = "https://api.github.com"
COMPONENTS = [
    "dracor-api",
    "dracor-frontend",
    "dracor-metrics",
    "dracor-fuseki",
    "dracor-schema",
    "dracor-mcp",
    "pydracor",
    "rdracor",
]
PYPI_PACKAGES = ["pydracor", "pydracor-base"]
CRAN_PACKAGES = ["rdracor"]
USER_AGENT = "dracor-textbook-versions-script"


def fetch(url, accept="application/json", github=False):
    headers = {"Accept": accept, "User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN")
    if github and token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        raw = response.read()
        if response.headers.get("Content-Encoding") == "gzip" or raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        data = raw.decode("utf-8")
    return json.loads(data) if "json" in accept else data


def github(path):
    try:
        return fetch(f"{GITHUB_API}/{path}", accept="application/vnd.github+json", github=True)
    except urllib.error.HTTPError as error:
        if error.code == 403:
            sys.exit("GitHub rate limit reached; set GITHUB_TOKEN (see --help).")
        return None


def commit_sha(repo, ref):
    commit = github(f"repos/{repo}/commits/{ref}")
    return commit["sha"] if commit else ""


def commit_date(repo, sha):
    commit = github(f"repos/{repo}/commits/{sha}")
    return commit["commit"]["committer"]["date"][:10] if commit else ""


# --- deployed software -----------------------------------------------------

def deployed_software(instance):
    info = fetch(f"{instance}/api/v1/info")
    frontend = "not found"
    try:
        html = fetch(instance + "/", accept="text/html")
        for script in re.findall(r'src="(/assets/[^"]+\.js)"', html):
            bundle = fetch(instance + script, accept="text/javascript")
            # The footer checks the front-end version before linking to its release.
            match = re.search(r"dracor-frontend/releases/`;return/.{0,80}?\.test\(`([^`]+)`\)", bundle)
            if match:
                frontend = match.group(1)
                break
    except urllib.error.URLError:
        pass
    return [
        ("DraCor API", info.get("version", ""), "`/api/v1/info`"),
        ("eXist-db", info.get("existdb", ""), "`/api/v1/info`"),
        ("DraCor front-end", frontend, "JavaScript bundle of the front-end"),
    ]


# --- releases --------------------------------------------------------------

def releases(repo):
    items = github(f"repos/{repo}/releases?per_page=30") or []
    items = [r for r in items if not r.get("draft")]
    stable = next((r for r in items if not r["prerelease"]), None)
    pre = next((r for r in items if r["prerelease"]), None)
    if pre and stable and pre["published_at"] < stable["published_at"]:
        pre = None  # an older pre-release is not of interest

    def describe(release):
        if not release:
            return "–"
        tag = release["tag_name"]
        return f"{tag} ({release['published_at'][:10]}), `{commit_sha(repo, tag)}`"

    return describe(stable), describe(pre)


def pypi(package):
    data = fetch(f"https://pypi.org/pypi/{package}/json")
    version = data["info"]["version"]
    files = data["releases"].get(version) or [{}]
    return version, (files[0].get("upload_time") or "")[:10]


def cran(package):
    html = fetch(f"https://cran.r-project.org/web/packages/{package}/index.html", accept="text/html")
    version = re.search(r"Version:</td>\s*<td>([^<]+)</td>", html)
    published = re.search(r"Published:</td>\s*<td>([^<]+)</td>", html)
    return (version.group(1) if version else "?"), (published.group(1) if published else "")


# --- corpora ---------------------------------------------------------------

def corpora(instance):
    rows = []
    for corpus in sorted(fetch(f"{instance}/api/v1/corpora?include=metrics"), key=lambda c: c["name"]):
        url = corpus.get("repository", "")
        repo, _, branch = url.replace("https://github.com/", "").partition("#")
        sha = corpus.get("commit", "")
        if not branch:
            info = github(f"repos/{repo}") or {}
            branch = info.get("default_branch", "main")
        head = github(f"repos/{repo}/commits/{branch}") or {}
        head_sha = head.get("sha", "")
        head_date = head.get("commit", {}).get("committer", {}).get("date", "")[:10]
        if sha and head_sha and sha != head_sha:
            compare = github(f"repos/{repo}/compare/{sha}...{head_sha}") or {}
            status = compare.get("status", "")
            if status == "ahead":
                state = f"{compare['ahead_by']} commit(s) not deployed"
            elif status == "behind":
                state = f"deployed commit is {compare['behind_by']} commit(s) ahead of `{branch}`"
            else:
                state = f"diverged from `{branch}`"
        else:
            state = "deployed"
        rows.append({
            "acronym": corpus.get("acronym") or corpus["name"],
            "name": corpus["name"],
            "plays": corpus.get("metrics", {}).get("plays", ""),
            "repo": repo,
            "sha": sha,
            "date": commit_date(repo, sha) if sha else "",
            "branch": branch,
            "head": head_sha,
            "head_date": head_date,
            "state": state,
        })
    return rows


# --- output ----------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--instance", default="https://dracor.org", help="DraCor instance (default: %(default)s)")
    args = parser.parse_args()
    instance = args.instance.rstrip("/")

    print(f"# DraCor versions ({instance}, {datetime.date.today().isoformat()})\n")

    print("## Software deployed on the instance\n")
    print("| Component | Version | Source |\n|---|---|---|")
    for name, version, source in deployed_software(instance):
        print(f"| {name} | {version} | {source} |")

    print("\n## Latest releases on GitHub\n")
    print("| Component | Latest stable release | Latest pre-release |\n|---|---|---|")
    for component in COMPONENTS:
        stable, pre = releases(f"dracor-org/{component}")
        print(f"| [{component}](https://github.com/dracor-org/{component}) | {stable} | {pre} |")
    print()
    for package in PYPI_PACKAGES:
        version, date = pypi(package)
        print(f"- PyPI `{package}`: {version} ({date})")
    for package in CRAN_PACKAGES:
        version, date = cran(package)
        print(f"- CRAN `{package}`: {version} ({date})")

    rows = corpora(instance)
    print(f"\n## Corpora ({len(rows)})\n")
    print("| Corpus | Plays | Deployed commit | Date | Latest commit in repository |\n|---|---|---|---|---|")
    for r in rows:
        link = f"[`{r['sha']}`](https://github.com/{r['repo']}/commit/{r['sha']})" if r["sha"] else "–"
        latest = f"`{r['head'][:7]}` on `{r['branch']}` ({r['head_date']}): {r['state']}"
        print(f"| {r['acronym']} (`{r['name']}`) | {r['plays']} | {link} | {r['date']} | {latest} |")


if __name__ == "__main__":
    main()
