#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Derek Rodger'
SITENAME = 'Devslant'
SITESUBTITLE = 'Obviously Obfuscated Originality'
SITEURL = 'http://devslant.com'

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
          ('Python.org', 'http://python.org/'),
          ('Django', 'https://djangoproject.com/'),
          ('Pelican', 'http://getpelican.com/'),)


LINKS_WIDGET_NAME = 'Professional profiles'
LINKS = (('GitHub', 'https://github.com/drodger'),
         ('LinkedIn', 'https://www.linkedin.com/in/devslant/'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['tipue_search', 'jinja2content', 'pelican_githubprojects', ]

GITHUB_USER = 'drodger'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False


TWITTER_USER = 'devslant'
TWITTER_WIDGET_ID = '438774350494183424'
# SEARCH_BOX = True
TIPUE_SEARCH = True

# THEME = 'themes/backdrop'
# THEME = 'themes/elegant'
# THEME = 'themes/lovers'
# THEME = 'themes/bricks'
# THEME = 'themes/built-texts'
# THEME = 'themes/gum'
# THEME = 'themes/lovers'
# THEME = 'themes/nest'
# THEME = 'themes/notmyidea-cms'
# THEME = 'themes/pelican-cait'
# THEME = 'themes/pelican-simplegrey'
# THEME = 'themes/pelican-striped-html5up'
# THEME = 'themes/pelican-twitchy'

THEME = 'themes/plumage'
# THEME = 'themes/octopress'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

TAG_RULE = 'tag/{slug}/'
# # PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')


RIGHT_SIDEBAR = """
"""
