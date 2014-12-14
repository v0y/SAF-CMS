from .settings_base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS.append('debug_toolbar')

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1', ]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

DEFAULT_THEME = 2

# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
