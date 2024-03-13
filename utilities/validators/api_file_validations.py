from pathlib import Path

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
    message = 'Длина текста должна быть меньше 3500'


class ApiMinLengthFileValidator(MinLengthFileValidator, ApiBaseValidator):
    message = 'Длина текста должна быть больше 50'


api_extension_validation = ApiFileExtensionValidator(('docx', 'pdf', 'txt'))
api_content_validation = ApiContentValidator(('application/pdf', 'application/zip', 'text/plain'))
api_max_size_validation = ApiMaxFileSizeValidation(2097152)
api_max_length_file_text = ApiMaxLengthFileValidator(3500)
api_min_length_file_text = ApiMinLengthFileValidator(50)


def validate_api_file(file):
    validators = (api_max_size_validation, api_content_validation, api_extension_validation, api_min_length_file_text,
                  api_max_length_file_text)
    for validator in validators:
        validator(file)
