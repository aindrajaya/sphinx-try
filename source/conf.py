# Configuration file for the Sphinx documentation builder.

project = 'Test'
copyright = '2023, pena'
author = 'pena'
release = '0.1'

extensions = [
    # 'sphinx.ext.toc',
]

templates_path = ['_templates']
exclude_patterns = []

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
        'sidebar.html',     # Custom sidebar template
    ],
}

# Define custom sidebar items
html_theme_options = {
    'navigation_with_keys': True,
}
