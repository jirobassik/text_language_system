from django.core.validators import MaxLengthValidator, MinLengthValidator
from utilities.validators.base_validator import ApiBaseValidator


class ApiMinLengthValidator(MinLengthValidator, ApiBaseValidator):
    message = 'Длина текста должна быть больше 50'


class ApiMaxLengthValidator(MaxLengthValidator, ApiBaseValidator):
    message = 'Длина текста должна быть не больше 1000'


api_max_length_validation = ApiMaxLengthValidator(1000)
api_min_length_validation = ApiMinLengthValidator(50)


def validate_api_text(text):
    validators = (api_max_length_validation, api_min_length_validation,)
    for validator in validators:
        validator(text)
