import json
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from ninja_extra import NinjaExtraAPI

from history.api.schems import HistoryOut
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from ninja_extra.throttling import throttle
from history.models import HistoryModel

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="History API",
    urls_namespace="history_api",
)


@api.exception_handler(ValidationError)
@api.exception_handler(Http404)
def validation_errors(request, exc):
    error_detail = {"detail": "Not found"}
    return HttpResponse(json.dumps(error_detail, ensure_ascii=False), status=404)


@api.get("/detail/{history_id}", response=HistoryOut)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def history_detail(request, history_id):
    history_obj = get_object_or_404(
        HistoryModel, id=history_id, user=request.user, is_deleted=False
    )
    return history_obj
