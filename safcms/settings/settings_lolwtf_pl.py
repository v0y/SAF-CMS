from .settings_base import *


STATIC_ROOT = join('/', 'var', 'www', 'lolwtf.pl', 'public', 'static')
MEDIA_ROOT = join('/', 'var', 'www', 'lolwtf.pl', 'public', 'media')

WSGI_APPLICATION = 'wsgi.application'

SITE_ID = 3
DEFAULT_THEME = 2

# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
