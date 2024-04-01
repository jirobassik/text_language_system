import json
from django.http import HttpResponseNotFound, HttpResponse
from django.views import View
from utilities.redis_com.redis_connect import r


class JsonView(View):
    def get(self, request):
        session_id = self.request.session.session_key
        if result := r.hgetall(f"user:{session_id}:json"):
            return self.gen_response(result)
        return HttpResponseNotFound()

    @staticmethod
    def gen_response(result: dict):
        response = HttpResponse(
            json.dumps(result, ensure_ascii=False), content_type="application/json"
        )
        response["Content-Disposition"] = f'attachment; filename="{result.get("app_name")}_res.json"'
        return response
