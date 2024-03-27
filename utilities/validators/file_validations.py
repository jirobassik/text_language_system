from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django import forms
from django.conf import settings
from utilities.file_manager.file import FileManager
from utilities.file_manager.file_type import file_type


class CleanMixin:
    def clean(self, x: object) -> object:
        try:
            return len(FileManager().file_read(x))
        except TypeError:
            raise forms.ValidationError("Не удалось прочитать файл")


class ContentValidator(FileExtensionValidator):
    message = "Неподдерживаемый тип файла"
    code = "invalid_content"

    def __call__(self, value):
        if not self.validate_content(value):
            raise forms.ValidationError(self.message)

    def validate_content(self, file):
        file_mime_type = file_type(file)
        return file_mime_type in self.allowed_extensions


class MaxFileSizeValidation(MaxValueValidator):
    message = "Размер файла должен быть не более 2 мб"

    def clean(self, x):
        return x.size


class MaxLengthFileValidator(CleanMixin, MaxLengthValidator):
    pass


class MinLengthFileValidator(CleanMixin, MinLengthValidator):
    pass


extension_validation = FileExtensionValidator(settings.VALID_EXTENSIONS_FILE)
content_validation = ContentValidator(settings.VALID_CONTENT_FILE)
max_size_validation = MaxFileSizeValidation(settings.VALID_MAX_FILE_SIZE)
max_length_file_text = MaxLengthFileValidator(settings.VALID_MAX_FILE_LENGTH_TEXT)
min_length_file_text = MinLengthFileValidator(settings.VALID_MIN_FILE_LENGTH_TEXT)
