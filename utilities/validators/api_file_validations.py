from pathlib import Path

from ninja.errors import ValidationError
from utilities.validators.file_validations import ContentValidator, MaxFileSizeValidation, FileExtensionValidator
from utilities.validators.base_validator import ApiBaseValidator

class ApiContentValidator(ContentValidator):

    def __call__(self, value):
        if not self.validate_content(value):
            raise ValidationError(self.message)


class ApiMaxFileSizeValidation(MaxFileSizeValidation, ApiBaseValidator):
    pass


class ApiFileExtensionValidator(FileExtensionValidator):

    def __call__(self, value):
        extension = Path(value.name).suffix[1:].lower()
        if (
                self.allowed_extensions is not None
                and extension not in self.allowed_extensions
        ):
            raise ValidationError(self.message)


api_extension_validation = ApiFileExtensionValidator(('docx', 'pdf', 'txt'))
api_content_validation = ApiContentValidator(('application/pdf', 'application/zip', 'text/plain'))
api_max_size_validation = ApiMaxFileSizeValidation(2097152)


def validate_api_file(file):
    validators = (api_max_size_validation, api_content_validation, api_extension_validation,)
    for validator in validators:
        validator(file)
