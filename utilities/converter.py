import json


def convert_to_serializable(data, **kwargs):
    return json.dumps(
        data,
        ensure_ascii=False,
        **kwargs
    )
