from django.conf import settings
from django.db.models import TextChoices
from ninja import Schema
from pydantic import Field
from utilities.api.docs.apps.summarize import *


class Methods(TextChoices):
    extractive = "extractive_plus"
    py_sum = "py_sum"


class Summarize(Schema):
    text: str = Field(
        default="",
        validate_default=False,
        min_length=settings.API_VALID_MIN_FORM_LENGTH_TEXT,
        max_length=settings.API_VALID_MAX_FORM_LENGTH_TEXT,
    )
    method: Methods = Methods.extractive
    num_sentences: int = Field(description=num_sentence_description, default=10, ge=10, le=100)


class SummarizeFile(Schema):
    method: Methods = Methods.extractive
    num_sentences: int = Field(description=num_sentence_description, default=10, ge=10, le=100)
