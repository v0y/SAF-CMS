import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

THEMES = (
    {
        'name': 'default',
        'description': 'Default theme',
        'screenshot': '',
        'template_dir': 'default',
        'static_url': '/static/default/',
    },
    {
        'name': 'lolwtf.pl',
        'description': 'Theme for lolwtf.pl site',
        'screenshot': '',
        'template_dir': 'lolwtf.pl',
        'static_url': '/static/lolwtf.pl/',
    }
)

DEFAULT_THEME = 0
