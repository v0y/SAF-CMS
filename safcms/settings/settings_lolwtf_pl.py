from .settings_base import *

WSGI_APPLICATION = 'wsgi.application'

# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
