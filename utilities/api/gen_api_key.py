from secrets import token_hex
from uuid import uuid4
from django.contrib.auth.hashers import make_password


def generate_api_key(key_len=64):
    prefix = uuid4()
    api_key = f"textproc.{prefix}.{token_hex(key_len)}"
    api_hash_key = make_password(api_key)
    return prefix, api_key, api_hash_key
