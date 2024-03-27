import json

from django.conf import settings
from django.db.models import TextChoices
from django.http import HttpResponse
from ninja import Schema, File, Form
from pydantic import Field
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from text_proc.sum_mod.methods import methods
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import User60MinRateThrottle, User100PerDayRateThrottle
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from ninja_extra.throttling import throttle
from utilities.api.docs.apps.summarize import *

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Summarize text API",
    urls_namespace="summarize_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_errors(request, exc: ValidationError):
    error_detail = {"detail": exc.errors}
    return HttpResponse(json.dumps(error_detail, ensure_ascii=False), status=422)


class Methods(TextChoices):
    extractive = "extractive_plus"
    py_sum = "py_sum"


class Summarize(Schema):
    text: str = Field(
        min_length=settings.API_VALID_MIN_FORM_LENGTH_TEXT,
        max_length=settings.API_VALID_MAX_FORM_LENGTH_TEXT,
    )
    method: Methods = Methods.extractive
    num_sentences: int = Field(description=num_sentence_description, default=10, ge=10, le=100)


class SummarizeFile(Schema):
    method: Methods = Methods.extractive
    num_sentences: int = Field(description=num_sentence_description, default=10, ge=10, le=100)


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
