"""Distinguish works by the same authors from the same year: 2026a, 2026b.

In the author-year style, two works by the same authors from the same year
look alike in the text, e.g. "(Börner, 2026)" for two different works. This
extension appends a letter to the year of such works, "(Börner, 2026a)" and
"(Börner, 2026b)", in the citations and in the reference lists (#84).

Two works get letters if their citations would look the same: the same
author names (or editor names, if there are no authors) as shown in the
text, i.e. up to two last names, or the first last name followed by "et al."
for three or more persons, and the same year. Within such a group, the
letters follow the alphabetical order of the titles. Only works that are
cited somewhere in the book are counted, and a work keeps its letter across
all chapters.

The original year is kept in the field ``yearbase``, so that the letters are
computed afresh on every build.
"""

from collections import defaultdict

from sphinx.util import logging

logger = logging.getLogger(__name__)

BASE_FIELD = "yearbase"


def _last_names(person):
    return " ".join(person.prelast_names + person.last_names)


def _label(entry):
    """The author part of a citation, as the author-year style shows it."""
    for role in ("author", "editor"):
        persons = entry.persons.get(role)
        if persons:
            names = [_last_names(p) for p in persons]
            if len(names) >= 3:
                return (names[0], "et al.")
            return tuple(names)
    return ("title:" + entry.fields.get("title", ""),)


def _plain(text):
    return "".join(ch for ch in str(text) if ch.isalnum() or ch.isspace()).lower()


def add_year_suffixes(app, env):
    domain = env.get_domain("cite")
    entries = domain.bibdata.data.entries
    cited = {
        target.key
        for ref in domain.citation_refs
        for target in ref.targets
        if target.key in entries
    }

    # Restore the original years (the data may come from the pickled env).
    for entry in entries.values():
        if BASE_FIELD in entry.fields:
            entry.fields["year"] = entry.fields[BASE_FIELD]

    groups = defaultdict(list)
    for key in cited:
        entry = entries[key]
        year = entry.fields.get("year")
        if year:
            groups[(_label(entry), year)].append(key)

    count = 0
    for (_, year), keys in groups.items():
        if len(keys) < 2:
            continue
        keys.sort(key=lambda k: (_plain(entries[k].fields.get("title", "")), k))
        for i, key in enumerate(keys):
            entry = entries[key]
            entry.fields[BASE_FIELD] = year
            entry.fields["year"] = year + "abcdefghijklmnopqrstuvwxyz"[i]
            count += 1
    if count:
        logger.info("bibtex_year_suffix: added a letter to the year of %d works", count)
    return []


def setup(app):
    # Before sphinxcontrib-bibtex formats labels and entries in its own
    # env-updated handler (default priority 500).
    app.connect("env-updated", add_year_suffixes, priority=400)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
