from .settings_base import *

# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
