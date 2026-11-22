"""Convert EzDrama markup to TEI/XML in the DraCor Textbook.

Used by the runnable examples in chapter 3 (section 4.3.6) and in exercise 3
of the self-test on TEI encoding. The conversion itself is done by the EzDrama
parser (`parser.py` in https://github.com/dracor-org/ezdrama). The parser is
not published as a package, so it is downloaded once at the commit pinned
below and cached in the user's home directory.

Its dependencies (beautifulsoup4, lxml, transliterate, yiddish and
setuptools<81) are listed in .binder/requirements.txt.
"""

from __future__ import annotations

import importlib.util
import pathlib
import re
import urllib.request
import warnings

EZDRAMA_COMMIT = "ec49e56693fa5aa796e3e8d2ce79ebb06a8629b9"
PARSER_URL = (
    f"https://raw.githubusercontent.com/dracor-org/ezdrama/{EZDRAMA_COMMIT}/parser.py"
)
CACHE_DIR = pathlib.Path.home() / ".cache" / "dracor-textbook" / f"ezdrama-{EZDRAMA_COMMIT[:7]}"

_parser_class = None


def _load_parser_class():
    """Download parser.py at the pinned commit (once) and return its Parser class."""
    global _parser_class
    if _parser_class is not None:
        return _parser_class
    path = CACHE_DIR / "parser.py"
    if not path.exists():
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(PARSER_URL, timeout=30) as response:
            path.write_bytes(response.read())
    spec = importlib.util.spec_from_file_location("ezdrama_parser", path)
    module = importlib.util.module_from_spec(spec)
    with warnings.catch_warnings():
        # The yiddish package imports pkg_resources, which warns on import.
        warnings.simplefilter("ignore")
        spec.loader.exec_module(module)
    _parser_class = module.Parser
    return _parser_class


def ezdrama_to_tei(ezdrama: str, full: bool = False) -> str:
    """Convert a text in EzDrama markup to TEI/XML.

    By default, only the parts discussed in chapter 3 are returned: the
    <listPerson> element generated for the <teiHeader> and the <body> element
    with the dramatic text. With full=True, the complete TEI document is
    returned, including the header template that the parser generates.
    """
    parser = _load_parser_class()()
    parser.parse_lines_to_xml(ezdrama.strip("\n").splitlines(keepends=True))
    tei = parser.tree_to_write
    if full:
        return tei
    parts = []
    for element in ("listPerson", "body"):
        match = re.search(rf"^( *)<{element}>.*?</{element}>", tei, re.S | re.M)
        if match:
            indent = len(match.group(1))
            lines = match.group(0).splitlines()
            parts.append("\n".join(line[indent:] if line.startswith(" " * indent) else line for line in lines))
    return "\n\n".join(parts)
