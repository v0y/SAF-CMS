from .settings_base import *

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = join('/', 'var', 'www', 'lolwtf.pl', 'public', 'static')
MEDIA_ROOT = join('/', 'var', 'www', 'lolwtf.pl', 'public', 'media')

WSGI_APPLICATION = 'wsgi.application'

SITE_ID = 2
DEFAULT_THEME = 1

# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
