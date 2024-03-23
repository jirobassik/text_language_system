from django.conf import settings
from django.core.cache import cache


def api_update_limit_check(user):
    key = f"user:{user}:update_limit"
    value = cache.get(key)
    if value is None:
        cache.set(key, 1, timeout=43200)
    elif value < settings.API_UPDATE_LIMIT:
        cache.incr(key)


def get_update_limit(user):
    key = f"user:{user}:update_limit"
    value = cache.get(key)
    return value if value is not None else 0


def check_limit(user):
    return True if get_update_limit(user) >= settings.API_UPDATE_LIMIT else False


def delete_limit(user):
    key = f"user:{user}:update_limit"
    if cache.has_key(key):
        cache.delete(key)
