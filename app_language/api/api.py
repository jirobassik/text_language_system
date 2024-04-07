from ninja import File, Form
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from app_language.api.schems import LanguageDet, LanguageDetFile
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
from langdetect.lang_detect_exception import LangDetectException
from utilities.api.error import send_error

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Language detector API",
    urls_namespace="lang_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_error(request, exc):
    return send_error(exc)


@api.exception_handler(LangDetectException)
def lang_detect_error(request, exc):
    exc.errors = lang_detect_error_message
    return send_error(exc)


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
