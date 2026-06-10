#
# conf.py
#
# Copyright The Ground Station Contributors.
#
# Ground Station Documentation
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
# International License. To view a copy of this license,
# visit http://creativecommons.org/licenses/by-sa/4.0/.
#
#

import sys
import ast

# Project information
project = 'grs-doc'
copyright = 'The Ground Station Contributors'
author = 'SpaceLab'
release = 'v0.1'
title = 'Ground Station'
doc_id = 'slb-grs-doc'

# General configuration
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

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Navigation bar title
html_title = "SpaceLab Ground Station"
html_short_title = "SpaceLab Ground Station"

# PDF output configuration
latex_documents = [
    (
        'pdf-index',                        # Root document (e.g., 'index' or 'pdf-index')
        doc_id + '-' + release + '.tex',    # Output LaTeX file name (no spaces)
        title,                              # Document title (can be empty to use the root doc's title)
        author,                             # Author name(s).
        'manual',                           # Document type: 'manual' or 'howto'
        True,                               # toctree_only: if True, only include docs in toctree
    ),
]

latex_logo = 'img/logo.jpg'

latex_toplevel_sectioning = 'chapter'
latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_elements_file = "_dev/latex_elements_custom.txt"

latex_elements = dict()

with open(latex_elements_file, "rt") as file:
    latex_config = file.read()
    if latex_elements == {}:
      latex_elements = ast.literal_eval(latex_config)

latex_additional_files = [
    '_dev/spacelab_book.sty',
    'img/by-sa.pdf',
    'img/spacelab-logo-full-color-rgb-1000px@72ppi.png',
]
