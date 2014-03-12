import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

THEMES = ({
    'name': 'default',
    'description': 'Default theme',
    'screenshot': '',
    'template_dir': 'default',
    'static_url': '/static/default/',
},
{
    'name': '3d.askra.pl',
    'description': 'Theme for 3d.askra.pl site',
    'screenshot': '',
    'template_dir': '3d.askra.pl',
    'static_url': '/static/3d.askra.pl/',
})

DEFAULT_THEME = 0
