import os  # noqa: D100
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "ImgVisFeat"
copyright = "2024, chatflip"
author = "chatflip"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

autodoc_typehints = "description"
autodoc_class_signature = "separated"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}
