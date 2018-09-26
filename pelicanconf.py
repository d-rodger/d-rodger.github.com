#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Derek Rodger'
SITENAME = 'Devslant'
SITESUBTITLE = 'Obviously Obfuscated Originality'
SITEURL = 'http://devslant.com'
# SITEURL = 'http://localhost:9000'

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'
LOCALE = 'C'
TYPOGRIFY = True
MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {'permalink': True},
        # 'mdx_video': {},
        # 'mdx_titlecase': {},
        # https://facelessuser.github.io/pymdown-extensions/
        # 'pymdownx.extra': {},
        # 'pymdownx.caret': {'superscript': True},
        # 'pymdownx.magiclink': {},
        # 'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
SOCIAL_WIDGET_NAME = 'Blog roll'
SOCIAL = (('Dan Bader', 'https://dbader.org/'),
          ('Python', 'https://python.org/'),
          ('Django', 'https://djangoproject.com/'),
          ('Pelican', 'https://getpelican.com/'),)


LINKS_WIDGET_NAME = 'Professional profiles'
LINKS = (('GitHub', 'https://github.com/drodger'),
         ('LinkedIn', 'https://linkedin.com/in/devslant/'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'tipue_search',
    'jinja2content',
    'pelican_githubprojects',
]

GITHUB_USER = 'drodger'
GITHUB_REPO_COUNT = 8

TIPUE_SEARCH = True

# THEME = 'themes/lovers'
# THEME = 'themes/built-texts'
# THEME = 'themes/nest'
# THEME = 'themes/pelican-cait'
# THEME = 'themes/pelican-simplegrey'
# THEME = 'themes/pelican-striped-html5up'
# THEME = 'themes/pelican-twitchy'

THEME = 'themes/plumage'
# THEME = 'themes/octopress'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

TAG_RULE = 'tag/{slug}/'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'search']

RIGHT_SIDEBAR = """
"""
