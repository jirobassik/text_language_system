import json
from django.http import HttpResponse, Http404
from django.core.exceptions import ValidationError
from ninja_extra import NinjaExtraAPI

from text_language_status.api.schems import StatusOut
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from ninja_extra.throttling import throttle
from text_language_status.models import TextLanguageManagerModel
from utilities.api.docs.apps.status import status_api_kwargs, description

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Status API",
    urls_namespace="status_api",
    description=description,
)


@api.exception_handler(ValidationError)
@api.exception_handler(Http404)
def validation_errors(request, exc):
    error_detail = {"detail": "Not found"}
    return HttpResponse(json.dumps(error_detail, ensure_ascii=False), status=404)


@api.get("/status/{status_id}", response=StatusOut, **status_api_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def status_detail(request, status_id):
    status_obj = TextLanguageManagerModel.objects.select_related("history_id").get(
        id=status_id, user=request.user, is_deleted=False
    )
    return status_obj
