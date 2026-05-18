# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx git documentation'
copyright = '2026, Emma'
author = 'Emma'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "Sphinx git documentation"
html_theme_options = {
}
extensions = [
    'sphinx_copybutton',
]
html_js_files = [
    ('js/custom-click.js', {'loading_method': 'defer'}),
]
html_css_files = [
    'css/custom-color.css',
]
# Déclaration globale des rôles de couleur pour tout le projet
rst_prolog = """
.. role:: red
.. role:: blue
.. role:: green
"""
# Masquer le bouton de copie uniquement pour les blocs de type "text"
copybutton_selector = "div:not(.highlight-text) > div.highlight pre"
