from django.template.defaultfilters import slugify as django_slugify


def slugify(string):
    """
    Slugify string

    :param string: string to slugify
    :return: slugified string
    """
    return django_slugify(string.replace('ł', 'l').replace('Ł', 'L'))


def shorten(s, max_len=50):
    if len(s) > max_len:
        return '%s…' % s[:max_len - 1]
    else:
        return s
