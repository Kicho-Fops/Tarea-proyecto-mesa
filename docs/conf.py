# noqa: D100
#!/usr/bin/env python3
#
# Mesa documentation build configuration file, created by
# sphinx-quickstart on Sun Jan  4 23:34:09 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import os.path as osp
import pathlib
import sys
import string
from datetime import date

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, "../mesa")


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",  # for google style docstrings
    "myst_nb",  # For Markdown and Jupyter notebooks
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Mesa"
copyright = f"2015-{date.today().year}, Project Mesa Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.5"
# The full version, including alpha/beta/rc tags.
release = ".1"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# Sort members by the order in the source files instead of alphabetically
autodoc_member_order = "bysource"

# Show both the class-level docstring and the constructor docstring
autoclass_content = "both"

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "gruvbox-dark"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

nb_execution_timeout = 60
nb_execution_mode = "cache"
nb_execution_allow_errors = False
nb_execution_raise_on_error = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "navbar_start": ["navbar-logo", "version-switcher"],  # Show switcher in navbar
    "switcher": {
        "json_url": "https://mesa.readthedocs.io/latest/_static/switcher.json",  # URL of your switcher.json file
        "version_match": version  # Automatically matches the current version
    }
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "images/mesa_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "images/mesa_logo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'migration_guide': [],  # No sidebar migration
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Mesadoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Mesa.tex", "Mesa Documentation", "Project Mesa Team", "manual")
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "mesa", "Mesa Documentation", ["Project Mesa Team"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Mesa",
        "Mesa Documentation",
        "Project Mesa Team",
        "Mesa",
        "One line description of project.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}



def write_example_md_file(agent_filename, model_filename, readme_filename, app_filename, md_filepath, template):
    with open(agent_filename) as content_file:
        agent_file = content_file.read()
    with open(model_filename) as content_file:
        model_file = content_file.read()
    with open(readme_filename) as content_file:
        readme_file = content_file.read()
    with open(app_filename) as content_file:
        app_file = content_file.read()

    with open(md_filepath, "w") as fh:
        content = template.substitute(
            dict(agent_file=agent_file, model_file=model_file,
                 readme_file=readme_file, app_file=app_file)
        )
        fh.write(content)

def setup_examples_pages():
    # create md files for all examples
    # check what examples exist
    examples_folder = osp.abspath(osp.join(HERE, "..", "mesa", "examples"))
    basic_examples = [("basic", f.path) for f in os.scandir(osp.join(examples_folder, "basic")) if f.is_dir() and not f.name.startswith("__") ]
    advanced_examples = [("advanced", f.path) for f in os.scandir(osp.join(examples_folder, "advanced")) if f.is_dir() and not f.name.startswith("__")]
    examples = basic_examples + advanced_examples

    with open(os.path.join(HERE, "example_template.txt")) as fh:
        template = string.Template(fh.read())

    root_folder = pathlib.Path(os.path.join(HERE, "examples"))
    root_folder.mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(root_folder, "basic")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(root_folder, "advanced")).mkdir(parents=True, exist_ok=True)

    examples_md = []
    for kind, example in examples:
        base_name = os.path.basename(os.path.normpath(example))

        agent_filename = os.path.join(example, "agents.py")
        model_filename = os.path.join(example, "model.py")
        readme_filename = os.path.join(example, "Readme.md")
        app_filename = os.path.join(example, "app.py")

        md_filename = f"{base_name}.md"
        examples_md.append((base_name, f"{kind}/{base_name}"))

        md_filepath = os.path.join(HERE, "examples", kind, md_filename)
        write_example_md_file(agent_filename, model_filename, readme_filename, app_filename, md_filepath, template)

    # create overview of examples.md
    with open(os.path.join(HERE, "examples_overview_template.txt")) as fh:
        template = string.Template(fh.read())

    with open(os.path.join(examples_folder, "README.md")) as fh:
        readme_md = fh.read()

    with open(os.path.join(HERE, "examples.md"), "w") as fh:
        content = template.substitute(
            dict(
                readme=readme_md,
                example_paths="\n".join([f"{' '.join(a.split('_'))} </examples/{b}>" for a, b in examples_md]),
            )
        )
        fh.write(content)

def setup(app):
    setup_examples_pages()

#
if __name__ == "__main__":
    setup_examples_pages()