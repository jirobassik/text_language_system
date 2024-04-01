import json
from django.http import HttpResponse
from ninja import File, Form
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from language_app.api.schems import LanguageDet, LanguageDetFile
from text_proc.lang_mod.methods import methods
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from ninja_extra.throttling import throttle
from utilities.api.docs.apps.language import *

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Language detector API",
    urls_namespace="lang_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    error_detail = {"detail": exc.errors}
    return HttpResponse(json.dumps(error_detail, ensure_ascii=False), status=422)


@api.post("/", **lang_detect_api_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def lang_detect_api_text(request, lang_text_schem: LanguageDet):
    res = methods.get(lang_text_schem.method.name)(lang_text_schem.text)
    return {"result": res}


@api.post("/file", **lang_detect_api_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def lang_detect_api_file(request, method: Form[LanguageDetFile], file: UploadedFile = File(...)):
    validate_api_file(file)
    res = methods.get(method.method.name)(ApiFIleManager().file_read(file))
    return {"result": res}
