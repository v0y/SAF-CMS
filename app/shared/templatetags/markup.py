from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown as markdown2html


register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    extensions = ["nl2br"]

    return mark_safe(markdown2html(
        value, extensions, safe_mode=True, enable_attributes=False))
