import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "safcms.settings.settings_default")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
