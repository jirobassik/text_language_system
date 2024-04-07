from ninja import File, Form
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI

from app_summarize.api.schems import Summarize, SummarizeFile
from text_proc.sum_mod.methods import methods
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import User60MinRateThrottle, User100PerDayRateThrottle
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from ninja_extra.throttling import throttle
from utilities.api.docs.apps.summarize import *
from utilities.api.error import send_error

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Summarize text API",
    urls_namespace="summarize_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_error(request, exc: ValidationError):
    return send_error(exc)


@api.post("/", **summarize_api_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def summarize_api_text(request, sum_text_schem: Summarize):
    res = methods.get(sum_text_schem.method.name)(sum_text_schem.text, sum_text_schem.num_sentences)
    return {"result": res}


@api.post("/file", **summarize_api_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def summarize_api_file(request, sum_text_file_schem: Form[SummarizeFile], file: File[UploadedFile]):
    validate_api_file(file)
    res = methods.get(sum_text_file_schem.method.name)(
        ApiFIleManager().file_read(file), sum_text_file_schem.num_sentences
    )
    return {"result": res}
