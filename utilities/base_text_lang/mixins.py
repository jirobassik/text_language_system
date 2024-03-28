from utilities.redis_com.redis_connect import r


class HsetMixin:

    @staticmethod
    def set_hset(session_key, result):
        r.hset(f"user:{session_key}:summarize", mapping={"result": result})
        r.expire(name=f"user:{session_key}:summarize", time=60)
