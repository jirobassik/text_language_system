from django.conf import settings
from utilities.redis_com.redis_connect import r
from utilities.redis_com.errors import MaxLongOperationsError


def setup_key(user):
    return f"long_operations:{user}"


def add_long_operation(user, oper_pk):
    r.rpush(setup_key(user), f"{oper_pk}")


def delete_long_operation(user, oper_pk):
    r.lrem(setup_key(user), 0, f"{oper_pk}")


def check_limit_long_operation(user):
    if r.llen(setup_key(user)) >= settings.MAX_LONG_OPERATIONS:
        raise MaxLongOperationsError("Max long operations exceeded")
