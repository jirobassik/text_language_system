from django.core.validators import FileExtensionValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django import forms
from django.conf import settings
import magic

from utilities.file_manager.file import FileManager

class CleanMixin:
    def clean(self, x):
        try:
            return len(FileManager().file_read(x))
        except TypeError:
            raise forms.ValidationError('Не удалось прочитать файл')

class ContentValidator(FileExtensionValidator):
    message = 'Неподдерживаемый тип файла'

    def __call__(self, value):
        if not self.validate_content(value):
            raise forms.ValidationError(self.message)

    def validate_content(self, file):
        file_object = file
        file_mime_type = magic.from_buffer(file_object.read(1024), mime=True)
        file_object.seek(0)
        return file_mime_type in self.allowed_extensions


class MaxFileSizeValidation(MaxValueValidator):
    message = 'Размер файла должен быть не более 2 мб'

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
