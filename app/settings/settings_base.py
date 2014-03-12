from os.path import dirname, join, realpath
import platform

_current_dir = dirname(realpath(__file__))


###############################################################################
# Basic settings
###############################################################################

IS_PRODUCTION = platform.node().endswith('vipserv.org')
DEBUG = not IS_PRODUCTION
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('voy', 'voyageur.pl@gmail.com'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']
SECRET_KEY = 'qpn8yh!vfg#waky9i+982^qc07u&939yt!52@)2t3sj92%gv$0'
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'passenger_wsgi.application'


###############################################################################
# Databases settings
###############################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.sqlite3',
    }
}

###############################################################################
# Localization settings
###############################################################################

TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'

# 1 - default
# 2 - 3d.askra.pl
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_INPUT_FORMATS = (
    '%H:%M:%S',
    '%H:%M',
    '%H.%M.%S',
    '%H.%M',
    '%H,%M,%S',
    '%H,%M',
)

###############################################################################
# Staticfiles/media/templates settings
###############################################################################

MEDIA_ROOT = join(_current_dir, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(_current_dir, '..', 'public', 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    join(_current_dir, '..', '..', 'vendor', 'OSB-CSS'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
)


###############################################################################
# Middleware, installed apps, processors
###############################################################################

MIDDLEWARE_CLASSES = [
    # core
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # third party
    'themes.middleware.ThemesMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    # core
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    # third party
    'themes.context_processors.themes',

    # internal
    'app.pages.context_processors.boxes',
    'app.pages.context_processors.menu'
]

INSTALLED_APPS = list(filter(None, [
    # core
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # third-party
    'debug_toolbar' if DEBUG else None,
    'fiut',
    'south',
    'themes',

    # internal
    'app.pages',
    'app.shared',
]))


###############################################################################
# third-party apps settings
###############################################################################

# django theme
from .themes_settings import *
THEMES_USE_TEMPLATE_LOADERS = False


# debug_toolbar
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INTERNAL_IPS = ['127.0.0.1', ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }
