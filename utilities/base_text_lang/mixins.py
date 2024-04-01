from utilities.redis_com.redis_connect import r


class HsetMixin:

    @staticmethod
    def set_hset(session_key, expire_time=60, **kwargs):
        r.hset(f"user:{session_key}:json", mapping=kwargs)
        r.expire(name=f"user:{session_key}:json", time=expire_time)
