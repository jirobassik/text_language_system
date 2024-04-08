import json

from ninja import File
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from app_sentiment.api.schems import SentimentSchem
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from langdetect.lang_detect_exception import LangDetectException
from ninja_extra.throttling import throttle
from utilities.api.error import send_error
from utilities.api.docs.apps.entities import (
    description,
    entities_extraction_api_file_kwargs,
    entities_extraction_api_text_kwargs,
    ent_extr_error_message,
)
from text_proc.ent_mod.entity_extraction import EntityExtraction


api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Entities extraction API",
    urls_namespace="ent_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_error(request, exc):
    return send_error(exc)


@api.exception_handler(LangDetectException)
def extraction_error(request, exc):
    exc.errors = ent_extr_error_message
    return send_error(exc)


@api.post("/", **entities_extraction_api_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def entities_extraction_api_text(request, lang_text_schem: SentimentSchem):
    res = EntityExtraction()(lang_text_schem.text)
    return {
        "result": json.dumps(
            res,
            default=list,
            ensure_ascii=False,
        )
    }


@api.post("/file", **entities_extraction_api_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def entities_extraction_api_file(request, file: UploadedFile = File(...)):
    validate_api_file(file)
    res = EntityExtraction()(ApiFIleManager().file_read(file))
    return {
        "result": json.dumps(
            res,
            default=list,
            ensure_ascii=False,
        )
    }
