import time

from django.conf import settings
from django.core.cache import cache


def get_throttle_value(user_pk):
    value = cache.get("throttle_%(scope)s_%(ident)s" % {"scope": "days", "ident": user_pk})
    return settings.USER_DAY_THROTTLE - len(value) if value else None


def get_throttle_duration(user_pk):
    value = cache.get("throttle_%(scope)s_%(ident)s" % {"scope": "days", "ident": user_pk})
    duration = 86400
    remaining_duration = duration - (time.time() - value[-1]) if value else duration
    return round(remaining_duration / 3600, 2)
