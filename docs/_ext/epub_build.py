"""Settings for the EPUB build of the textbook.

Build with:

    jupyter-book build docs --builder custom --custom-builder epub

The EPUB contains the chapters and the appendix. The self-tests are
interactive (quizzes in JavaScript, answer boxes), which e-book readers do
not support. In the EPUB each self-test page therefore keeps only its title
and a link to the online version, and links from the chapters to the
self-tests point to the online version, too.

Launch buttons make no sense in an e-book either. sphinx-book-theme adds them
in every builder, and in the EPUB builder it fails with "cannot unpack
non-iterable NoneType object", so they are switched off.
"""

from posixpath import normpath, relpath, splitext

from docutils import nodes

ONLINE_URL = "https://textbook.dracor.org/"
SELF_TEST_DIR = "assessment/"


def configure_epub(app):
    if app.builder.name != "epub":
        return
    config = app.config
    config.html_theme_options = {
        **config.html_theme_options,
        "launch_buttons": {},
    }
    # Nothing in the EPUB needs executed notebooks: the chapters are not
    # executed and the self-tests are replaced by a link.
    config.nb_execution_mode = "off"


def is_self_test(docname):
    return docname.startswith(SELF_TEST_DIR)


def online_url(docname, anchor=""):
    return ONLINE_URL + docname + ".html" + (f"#{anchor}" if anchor else "")


def replace_self_test(app, doctree, docname):
    section = next(iter(doctree.findall(nodes.section)), None)
    if section is None:
        return
    title = section.next_node(nodes.title)
    url = online_url(docname)
    note = nodes.paragraph()
    note += nodes.Text(
        "This self-test is interactive and is not included in the EPUB. "
        "You can take it in the online version of the textbook: "
    )
    note += nodes.reference(url, url, refuri=url)
    note += nodes.Text(".")
    section.children = [title, note] if title is not None else [note]


def link_self_tests_online(app, doctree, docname):
    builder = app.builder
    for ref in doctree.findall(nodes.reference):
        uri = ref.get("refuri", "")
        if not uri or "://" in uri or uri.startswith(("#", "mailto:")):
            continue
        path, _, anchor = uri.partition("#")
        if not path:
            continue
        # Resolve the relative link against the current page.
        current = builder.get_target_uri(docname)
        target = normpath(relpath(path, ".") if current.count("/") == 0
                          else current.rsplit("/", 1)[0] + "/" + path)
        target_doc = splitext(target)[0]
        if is_self_test(target_doc):
            ref["refuri"] = online_url(target_doc, anchor)
            ref["internal"] = False


def on_doctree_resolved(app, doctree, docname):
    if app.builder.name != "epub":
        return
    if is_self_test(docname):
        replace_self_test(app, doctree, docname)
    else:
        link_self_tests_online(app, doctree, docname)


def setup(app):
    # Before myst-nb reads nb_execution_mode in its builder-inited handler
    # (default priority 500).
    app.connect("builder-inited", configure_epub, priority=400)
    app.connect("doctree-resolved", on_doctree_resolved)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
