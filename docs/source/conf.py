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

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "example_pkg_winksaville"
copyright = "2020, Wink Saville"
author = "Wink Saville"

# The full version, including alpha/beta/rc tags
release = "0.1.0"

# -- Filter issue 123 related to dataclasses ---------------------------
# FROM: https://github.com/agronholm/sphinx-autodoc-typehints/issues/123#issuecomment-698314873
#
# Probable Real Fix: https://github.com/agronholm/sphinx-autodoc-typehints/pull/153
# I was able to supress the warning by adding the following code which is just like pull 153:
#    # The generated dataclass __init__() is weird and needs second condition
#    # if '<locals>' in obj.__qualname__ and not (what == 'method' and name.endswith('.__init__')):
#    if '<locals>' in obj.__qualname__ and not (
#        (what == 'method' and name.endswith('.__init__'))
#        or (what == 'class' and obj.__qualname__.endswith('.__init__'))
#    ):
#        logger.warning(f"WINK: app={app} what={what} name={name} obj.__qualname_={obj.__qualname__} options={options} signature={signature} return_ann={return_annotation}")
#        logger.warning(
#            'Cannot treat a function defined as a local function: "%s"  (use @functools.wraps)',
#            name)
#        return

import logging as pylogging

from sphinx.util import logging


# Workaround for https://github.com/agronholm/sphinx-autodoc-typehints/issues/123
# When this https://github.com/agronholm/sphinx-autodoc-typehints/pull/153
# gets merged, we can remove this
class FilterForIssue123(pylogging.Filter):
    def filter(self, record: pylogging.LogRecord) -> bool:
        # You probably should make this check more specific by checking
        # that dataclass name is in the message, so that you don't filter out
        # other meaningful warnings
        return not record.getMessage().startswith("Cannot treat a function")


# Register the fliter
logging.getLogger("sphinx_autodoc_typehints").logger.addFilter(FilterForIssue123())
# End of a workaround


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # Auto docs "always needed"
    "sphinx_autodoc_typehints",  # Handle typehints properly :)
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Extension configuration -------------------------------------------------
