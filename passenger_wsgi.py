###############################################################################
# passenger_wsgi.py for django app hosted on vipserv.org
###############################################################################

import os
import site
import sys


show_errors = True

# django app name
app_name = 'app'

# vipserv.org account login
account_login = 'mironczyk'

os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib'

# main site-packages based on site module
site.addsitedir('/home/%s/site-packages' % account_login)

# app directory
sys.path.insert(0, os.getcwd())

# site-packages directory in app directory
sys.path.insert(0, os.path.join(os.getcwd(), '/site-packages'))

# same as above but through site (if you installed there via easy_install)
site.addsitedir(os.path.join(os.getcwd(), '/site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % app_name)

# need to be imported after setting DJANGO_SETTINGS_MODULE
import django.core.handlers.wsgi

if show_errors:
    try:
        # run with visible errors (python 3.3)
        import ErrorMiddlewareV
        application = ErrorMiddlewareV.EMV(
            django.core.handlers.wsgi.WSGIHandler(), True)
    except ImportError:
        # run with visible errors (python 2.7 i 2.6)
        from paste.exceptions.errormiddleware import ErrorMiddleware
        application = django.core.handlers.wsgi.WSGIHandler()
        application = ErrorMiddleware(application, debug=True)
else:
    # run with hidden errors
    application = django.core.handlers.wsgi.WSGIHandler()
