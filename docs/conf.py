# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from importlib import metadata

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("_ext"))
# sys.path.append(os.abspath(os.join(os.dirname(__file__), "_ext")))

project = "xsData"
copyright = "2021, Christodoulos Tsoulloftas"
author = "Christodoulos Tsoulloftas"

# The full version, including alpha/beta/rc tags
version = release = metadata.version("xsdata")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "xsdatadocs",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# Required theme setup
# extensions.append("sphinx_material")
html_theme = "furo"
html_favicon = "_static/favicon.png"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo.svg",
    "dark_logo": "logo-dark.svg",
}

html_show_sourcelink = True
html_extra_path = ["robots.txt"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "lxml": ("https://lxml.de/apidoc/", None),
}

autodoc_default_options = {
    "member-order": "bysource",
    "special-members": None,
    # Exclude "standard" methods.
    "exclude-members": "__dict__,__weakref__,__init__,__repr__,__new__",
}

autosummary_generate = True
set_type_checking_flag = True
always_document_param_types = False
