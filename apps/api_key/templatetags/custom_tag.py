from django import template

from utilities.api.value_throttle import get_throttle_value, get_throttle_duration

register = template.Library()


@register.simple_tag
def get_throttle_value_html(user_pk):
    return get_throttle_value(user_pk)


@register.simple_tag
def get_throttle_value_duration_html(user_pk):
    return get_throttle_duration(user_pk)
