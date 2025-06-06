import json
from django.http import HttpResponseNotFound, HttpResponse
from django.views import View
from utilities.redis_com.redis_connect import r


class BaseFileView(View):
    def get(self, request):
        session_id = self.request.session.session_key
        if result := r.hgetall(f"user:{session_id}:json"):
            return self.gen_response(result)
        return HttpResponseNotFound()

    @staticmethod
    def gen_response(result: dict):
        raise NotImplementedError()


class JsonView(BaseFileView):

    @staticmethod
    def gen_response(result: dict):
        response = HttpResponse(
            json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True),
            content_type="application/json",
        )
        response["Content-Disposition"] = (
            f'attachment; filename="{result.get("app_name", "textproc")}_res.json"'
        )
        return response

class TxtView(BaseFileView):

    @staticmethod
    def gen_response(result: dict):
        response = HttpResponse(
            "".join(f"{key}: {value}\n" for key, value in result.items()),
            content_type="text/plain",
        )
        response["Content-Disposition"] = (
            f'attachment; filename="{result.get("app_name", "textproc")}_res.txt"'
        )
        return response
