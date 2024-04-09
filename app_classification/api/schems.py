from django.conf import settings
from ninja import Schema
from pydantic import Field


class ClassifySchem(Schema):
    text: str = Field(
        default="",
        validate_default=False,
        min_length=settings.API_VALID_MIN_FORM_LENGTH_TEXT,
        max_length=settings.API_VALID_MAX_FORM_LENGTH_TEXT,
    )
