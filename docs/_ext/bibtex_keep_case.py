"""Titles in the bibliography as they are in references.bib.

The default style of sphinxcontrib-bibtex (pybtex's "alpha") converts most
titles to sentence case: everything after the first letter is lowercased
unless it is protected by braces. This breaks German titles and proper names
("Digitalisierte sammlungen der staatsbibliothek zu berlin", #30). The
titles in references.bib are exported from Zotero with the intended
capitalisation, so this extension registers the style ``alpha_keep_case``,
which is the "alpha" style without the case conversion. It is selected in
_config.yml with ``bibtex_default_style: alpha_keep_case``.
"""

import pybtex.plugin
from pybtex.style.formatting.alpha import Style as AlphaStyle
from pybtex.style.template import field, sentence


class AlphaKeepCaseStyle(AlphaStyle):
    def format_title(self, e, which_field, as_sentence=True):
        formatted_title = field(which_field)
        if as_sentence:
            return sentence[formatted_title]
        return formatted_title


def setup(app):
    pybtex.plugin.register_plugin(
        "pybtex.style.formatting", "alpha_keep_case", AlphaKeepCaseStyle
    )
    return {"parallel_read_safe": True, "parallel_write_safe": True}
