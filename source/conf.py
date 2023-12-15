# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2023, pena'
author = 'pena'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   'sphinx.ext.toc',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']

# Add or modify the html_sidebars option
html_sidebars = {
    '**': [
        'globaltoc.html',   # Table of contents for the entire documentation
        'relations.html',   # Cross-references
        'sourcelink.html',  # Link to source code
        'searchbox.html',   # Search box
        'localtoc.html',    # On This Page sidebar
        'custom_sidebar.html',  # Custom sidebar template
    ],
}

# Define custom sidebar items
html_theme_options = {
    'navigation_with_keys': True,
}

