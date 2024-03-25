from secrets import token_hex
from django.contrib.auth.hashers import make_password


def generate_api_key(user_id, key_len=64):
    api_key = f"textproc-{user_id}-{token_hex(key_len)}"
    hash_key = make_password(api_key)
    return api_key, hash_key
