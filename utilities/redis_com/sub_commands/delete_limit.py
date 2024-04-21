from django.conf import settings
from utilities.redis_com.redis_connect import r
from utilities.redis_com.errors import MaxDeleteLimitError


def define_key_name(user):
    return f"user:{user}:update_limit"


def get_delete_limit(user):
    key = define_key_name(user)
    value = r.get(key)
    return int(value) if value is not None else 0


def api_delete_limit_check(user):
    key = define_key_name(user)
    value = get_delete_limit(user)
    if not value:
        r.set(key, 1, ex=43200)
    elif value < settings.API_UPDATE_LIMIT:
        r.incr(key)


def check_limit(user):
    return True if get_delete_limit(user) >= settings.API_UPDATE_LIMIT else False


def delete_limit(user):
    key = define_key_name(user)
    if r.has_key(key):
        r.delete(key)


def check_limit_error(user):
    if check_limit(user):
        raise MaxDeleteLimitError("Превышен лимит удалений")
