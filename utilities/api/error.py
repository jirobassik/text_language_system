import json

from django.http import HttpResponse


def send_error(exc, code=422):
    error_detail = {"detail": exc.errors}
    return HttpResponse(json.dumps(error_detail, ensure_ascii=False), status=code)
