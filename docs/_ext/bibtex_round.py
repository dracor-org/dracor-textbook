"""Author-year citations in round brackets.

The author_year style of sphinxcontrib-bibtex uses square brackets:
"[Fischer et al., 2019]", "Fischer et al. [2019]". The guidelines of the
DraCor Textbook expect round brackets. This extension registers the style
``author_year_round``, which is selected in _config.yml with
``bibtex_reference_style: author_year_round``.

See https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#custom-inline-citation-references
"""

import dataclasses

import sphinxcontrib.bibtex.plugin
from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year import AuthorYearReferenceStyle


def round_brackets() -> BracketStyle:
    return BracketStyle(left="(", right=")")


@dataclasses.dataclass
class AuthorYearRoundReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = dataclasses.field(default_factory=round_brackets)
    bracket_textual: BracketStyle = dataclasses.field(default_factory=round_brackets)
    bracket_author: BracketStyle = dataclasses.field(default_factory=round_brackets)
    bracket_label: BracketStyle = dataclasses.field(default_factory=round_brackets)
    bracket_year: BracketStyle = dataclasses.field(default_factory=round_brackets)


def setup(app):
    sphinxcontrib.bibtex.plugin.register_plugin(
        "sphinxcontrib.bibtex.style.referencing",
        "author_year_round",
        AuthorYearRoundReferenceStyle,
    )
    return {"parallel_read_safe": True, "parallel_write_safe": True}
