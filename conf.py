# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import ast

project = 'grs-doc'
copyright = '2025, SpaceLab'
author = 'SpaceLab'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig = True

extensions = ['sphinxcontrib.bibtex']

# Path to your .bib file
bibtex_bibfiles = ['references.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Identify the Sphinx builder being used
if '-b' in sys.argv:
    builder = sys.argv[sys.argv.index('-b') + 1]
elif '-M' in sys.argv:
    builder = sys.argv[sys.argv.index('-M') + 1]
else:
    builder = 'html'  # default builder

# Exclude the PDF-specific index from the HTML build
if builder in ['html', 'dirhtml']:
    exclude_patterns.append('pdf-index.rst')

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Navigation bar title
html_title = "SpaceLab Ground Station"
html_short_title = "SpaceLab Ground Station"

# PDF output configuration
latex_documents = [
    (
        'pdf-index',                        # Root document (e.g., 'index' or 'pdf-index')
        'slb-grs-doc-' + release + '.tex',  # Output LaTeX file name (no spaces)
        'SpaceLab Ground Station',          # Document title (can be empty to use the root doc's title)
        'SpaceLab',                         # Author name(s).
        'manual',                           # Document type: 'manual' or 'howto'
        False,                              # toctree_only: if True, only include docs in toctree
    ),
]

latex_logo = 'img/logo.jpg'

latex_toplevel_sectioning = 'chapter'
latex_show_pagerefs = True
latex_show_urls = 'footnote'

# Replace with the path to your local override file
latex_elements_file = "_dev/latex_elements_custom.txt"

latex_elements = dict()

with open(latex_elements_file, "rt") as file:
    latex_config = file.read()
    if latex_elements == {}:
      latex_elements = ast.literal_eval(latex_config)
