from django.core.validators import FileExtensionValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django import forms
import magic

from utilities.file_manager.file import FileManager


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


class MaxLengthFileValidator(MaxLengthValidator):
    def clean(self, x):
        return len(FileManager().file_read(x))


class MinLengthFileValidator(MinLengthValidator):

    def clean(self, x):
        return len(FileManager().file_read(x))


extension_validation = FileExtensionValidator(('docx', 'pdf', 'txt'))
content_validation = ContentValidator(('application/pdf', 'application/zip', 'text/plain'))
max_size_validation = MaxFileSizeValidation(2097152)
max_length_file_text = MaxLengthFileValidator(3500)
min_length_file_text = MinLengthFileValidator(50)
