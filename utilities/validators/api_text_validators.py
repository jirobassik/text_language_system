from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator

from utilities.validators.base_validator import ApiBaseValidator


class ApiMinLengthValidator(MinLengthValidator, ApiBaseValidator):
    message = f"Длина текста должна быть больше {settings.API_VALID_MIN_FORM_LENGTH_TEXT}"


class ApiMaxLengthValidator(MaxLengthValidator, ApiBaseValidator):
    message = f"Длина текста должна быть не больше {settings.API_VALID_MIN_FORM_LENGTH_TEXT}"


api_max_length_validation = ApiMaxLengthValidator(settings.API_VALID_MAX_FORM_LENGTH_TEXT)
api_min_length_validation = ApiMinLengthValidator(settings.API_VALID_MIN_FORM_LENGTH_TEXT)


def validate_api_text(text):
    validators = (
        api_max_length_validation,
        api_min_length_validation,
    )
    for validator in validators:
        validator(text)
