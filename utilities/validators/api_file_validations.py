from pathlib import Path
from django.conf import settings
from ninja.errors import ValidationError
from utilities.validators.file_validations import ContentValidator, MaxFileSizeValidation, FileExtensionValidator, \
    MinLengthFileValidator, MaxLengthFileValidator
from utilities.validators.base_validator import ApiBaseValidator


class ApiContentValidator(ContentValidator):

    def __call__(self, value):
        if not self.validate_content(value):
            raise ValidationError(self.message)


class ApiFileExtensionValidator(FileExtensionValidator):

    def __call__(self, value):
        extension = Path(value.name).suffix[1:].lower()
        if (
                self.allowed_extensions is not None
                and extension not in self.allowed_extensions
        ):
            raise ValidationError(self.message)


class ApiMaxFileSizeValidation(MaxFileSizeValidation, ApiBaseValidator):
    pass


class ApiMaxLengthFileValidator(MaxLengthFileValidator, ApiBaseValidator):
    message = f'Длина текста должна быть меньше {settings.API_VALID_MAX_FILE_LENGTH_TEXT}'


class ApiMinLengthFileValidator(MinLengthFileValidator, ApiBaseValidator):
    message = f'Длина текста должна быть больше {settings.API_VALID_MIN_FILE_LENGTH_TEXT}'


api_extension_validation = ApiFileExtensionValidator(settings.API_VALID_EXTENSIONS_FILE)
api_content_validation = ApiContentValidator(settings.API_VALID_CONTENT_FILE)
api_max_size_validation = ApiMaxFileSizeValidation(settings.API_VALID_MAX_FILE_SIZE)
api_max_length_file_text = ApiMaxLengthFileValidator(settings.API_VALID_MAX_FILE_LENGTH_TEXT)
api_min_length_file_text = ApiMinLengthFileValidator(settings.API_VALID_MIN_FILE_LENGTH_TEXT)


def validate_api_file(file):
    validators = (api_max_size_validation, api_content_validation, api_extension_validation, api_min_length_file_text,
                  api_max_length_file_text)
    for validator in validators:
        validator(file)
