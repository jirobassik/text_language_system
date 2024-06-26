import copy

from django.core.files.uploadedfile import InMemoryUploadedFile
from django import forms
from ninja import errors

from utilities.file_manager.file_type import file_type
from utilities.file_manager.readers.docx_reader import DocxReader
from utilities.file_manager.readers.pdf_reader import PdfReader
from utilities.file_manager.readers.txt_reader import TxtReader
from utilities.api.docs.common import common_file_error_message

class FileManager:
    error_message = "Не удалось прочитать файл"

    def file_read(self, file: InMemoryUploadedFile):
        file_copy = copy.deepcopy(file)
        match file_type(file_copy):
            case "application/zip":
                return DocxReader.read(file_copy)
            case "application/pdf":
                return PdfReader.read(file_copy)
            case "text/plain":
                try:
                    return TxtReader.read(file_copy)
                except UnicodeDecodeError:
                    raise self.read_error()
        raise self.read_error()

    def read_error(self):
        return forms.ValidationError(self.error_message)


class ApiFIleManager(FileManager):
    error_message = common_file_error_message

    def read_error(self):
        return errors.ValidationError(self.error_message)
