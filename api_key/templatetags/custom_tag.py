from django import template
from utilities.api.value_throttle import get_throttle_value

register = template.Library()


@register.simple_tag
def get_throttle_value_html(user_pk):
    return get_throttle_value(user_pk)
