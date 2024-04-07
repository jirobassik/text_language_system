from django.db.models import TextChoices
from django.conf import settings
from ninja import Schema
from pydantic import Field

initial_text = """I am living with a very welcoming host family. I have my own private bedroom, but we eat breakfast."""


class Methods(TextChoices):
    short = "short_word"
    langid = "langid"
    langdetect = "lang_detect"


class LanguageDet(Schema):
    text: str = Field(
        default=initial_text,
        min_length=settings.API_VALID_MIN_FORM_LENGTH_TEXT,
        max_length=settings.API_VALID_MAX_FORM_LENGTH_TEXT,
    )
    method: Methods = Methods.short


class LanguageDetFile(Schema):
    method: Methods = Methods.short
