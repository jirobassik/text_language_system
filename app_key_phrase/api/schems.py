from django.conf import settings
from ninja import Schema
from pydantic import Field
from utilities.api.docs.apps.key_phrase import num_key_phrases_description

initial_text = """I am living with a very welcoming host family. I have my own private bedroom, but we eat breakfast."""


class KeyPhraseSchem(Schema):
    text: str = Field(
        default=initial_text,
        min_length=settings.API_VALID_MIN_FORM_LENGTH_TEXT,
        max_length=settings.API_VALID_MAX_FORM_LENGTH_TEXT,
    )
    num_key_phrase: int = Field(description=num_key_phrases_description, default=5, ge=5, le=50)


class KeyPhraseSchemFile(Schema):
    num_key_phrase: int = Field(description=num_key_phrases_description, default=5, ge=5, le=50)
