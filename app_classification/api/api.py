from ninja import File, UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from app_classification.api.schems import ClassifySchem
from app_classification.api.start_class import ClassifyApiStart
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import User60MinRateThrottle, User100PerDayRateThrottle
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from ninja_extra.throttling import throttle
from utilities.redis_com.errors import MaxLongOperationsError
from utilities.api.error import send_error
from utilities.api.docs.apps.classify import *

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Classify text API",
    urls_namespace="classification_api",
    description=description,
    version="2.0",
)


@api.exception_handler(ValidationError)
@api.exception_handler(MaxLongOperationsError)
def validation_errors(request, exc):
    return send_error(exc)


@api.post("/", **classify_api_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def classify_api_text(request, clas_text_schem: ClassifySchem):
    task_id = ClassifyApiStart(request)(clas_text_schem.text)
    return {
        "result": task_id,
        "detail": "This long task. Check execution and get result in status api",
    }


@api.post("/file", **classify_api_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def classify_api_file(request, file: File[UploadedFile]):
    validate_api_file(file)
    task_id = ClassifyApiStart(request)(ApiFIleManager().file_read(file))
    return {
        "result": task_id,
        "detail": "This long task. Check execution and get result in status api",
    }
