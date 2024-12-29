from django.utils.translation import get_language
from django import template

register = template.Library()


@register.simple_tag
def language():
    return get_language()
