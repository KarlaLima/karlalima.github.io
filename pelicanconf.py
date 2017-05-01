#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Karla Lima'
SITENAME = u'Prof\xaa. Karla Lima'
SITEURL = ''
INSTITUTION = 'FACET - UFGD'
EMAIL = 'karlalima@ufgd.edu.br'
SEMESTRE = '2017.1'

PATH = 'content'

TIMEZONE = 'America/Campo_Grande'
DEFAULT_DATE = 'fs'

THEME = 'themes/prologue'
THEME_STATIC_DIR = ''

STATIC_PATHS = ['imagens', 'arquivos']

SLUGIFY_SOURCE = 'basename'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVE_SAVE_AS = ''
DIRECT_TEMPLATES = ['index']

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('email', 'mailto:' + EMAIL),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
