from .settings_base import *

# email
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = 'formularz@askra.pl'
EMAIL_HOST = 'askra.pl'
# EMAIL_HOST_PASSWORD in settings_local

DEFAULT_THEME = 1
SITE_ID = 2

TEMPLATE_CONTEXT_PROCESSORS += [
    'app.mails.context_processors.contact_form',
]


# import local settings
try:
    from .settings_local import *
except ImportError:
    pass
