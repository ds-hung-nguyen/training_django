from django import template

register = template.Library()


@register.simple_tag
def constants(key, default=''):
    from apps.support.helper import constants
    return constants(key, default)
