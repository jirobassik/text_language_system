from django.core.cache import cache


def get_throttle_value(user_pk):
    value = cache.get("throttle_%(scope)s_%(ident)s" % {'scope': 'days', 'ident': user_pk})
    return len(value) if value else 0
