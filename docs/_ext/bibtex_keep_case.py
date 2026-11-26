"""Bibliography style of the textbook: titles as in references.bib.

The default style of sphinxcontrib-bibtex (pybtex's "alpha") converts most
titles to sentence case: everything after the first letter is lowercased
unless it is protected by braces. This breaks German titles and proper names
("Digitalisierte sammlungen der staatsbibliothek zu berlin", #30). The
titles in references.bib are exported from Zotero with the intended
capitalisation, so this extension registers the style ``alpha_keep_case``,
which is the "alpha" style without the case conversion. It is selected in
_config.yml with ``bibtex_default_style: alpha_keep_case``.

The style also shows the editors of ``@misc`` entries that have no author,
e.g. websites edited by a team or RFCs edited by their editors; the "alpha"
style leaves them out.
"""

import pybtex.plugin
from pybtex.style.formatting.alpha import Style as AlphaStyle
from pybtex.style.template import field, optional, sentence


class AlphaKeepCaseStyle(AlphaStyle):
    def format_title(self, e, which_field, as_sentence=True):
        formatted_title = field(which_field)
        if as_sentence:
            return sentence[formatted_title]
        return formatted_title

    def get_misc_template(self, e):
        template = super().get_misc_template(e)
        if "author" not in e.persons and "editor" in e.persons:
            # Put the editors where the "alpha" style puts the authors.
            template.children[0] = optional[self.format_editor(e)]
        return template


def setup(app):
    pybtex.plugin.register_plugin(
        "pybtex.style.formatting", "alpha_keep_case", AlphaKeepCaseStyle
    )
    return {"parallel_read_safe": True, "parallel_write_safe": True}
