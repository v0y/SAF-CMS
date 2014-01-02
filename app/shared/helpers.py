from django.template.defaultfilters import slugify as django_slugify


def slugify(string):
    """
    Slugify string

    :param string: string to slugify
    :return: slugified string
    """
    return django_slugify(string.replace(u'ł', 'l').replace(u'Ł', 'L'))
