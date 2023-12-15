# -- Path setup --------------------------------------------------------------

import os
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from distutils.version import LooseVersion

import sphinx_material

FORCE_CLASSIC = os.environ.get("SPHINX_MATERIAL_FORCE_CLASSIC", False)
FORCE_CLASSIC = FORCE_CLASSIC in ("1", "true")

# Configuration file for the Sphinx documentation builder.

project = 'Test'
copyright = '2023, pena'
author = 'pena'
release = '0.1'

# The full version, including alpha/beta/rc tags
release = LooseVersion(sphinx_material.__version__).vstring

extensions = [
    # 'sphinx.ext.toc',
]

autosummary_generate = True
autoclass_content = "class"

templates_path = ['_templates']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = 'sphinx_material'
html_static_path = ['_static']

# Add or modify the html_sidebars option
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()

# Define custom sidebar items
html_theme_options = {
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "repo_type": "github",
    "globaltoc_depth": 2,
    "color_primary": "blue",
    "color_accent": "cyan",
}

if FORCE_CLASSIC:
    print("!!!!!!!!! Forcing classic !!!!!!!!!!!")
    html_theme = "classic"
    html_theme_options = {}
    html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True
html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        None,
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", None),
    "dudir": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s",
        None,
    ),
}

# Enable eval_rst in markdown
def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
