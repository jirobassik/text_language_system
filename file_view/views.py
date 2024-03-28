import json
from django.http import HttpResponseNotFound, HttpResponse
from django.views import View
from utilities.redis_com.redis_connect import r


class JsonView(View):
    def get(self, request):
        session_id = self.request.session.session_key
        if result := r.hgetall(f"user:{session_id}:summarize"):
            return self.gen_response(result)
        return HttpResponseNotFound()

    @staticmethod
    def gen_response(result: dict):
        response = HttpResponse(
            json.dumps(result, ensure_ascii=False), content_type="application/json"
        )
        response["Content-Disposition"] = 'attachment; filename="summarize_res.json"'
        return response
