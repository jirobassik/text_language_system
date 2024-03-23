from django.core.files.uploadedfile import InMemoryUploadedFile

from utilities.file_manager.file_type import file_type
from utilities.file_manager.readers.docx_reader import DocxReader
from utilities.file_manager.readers.pdf_reader import PdfReader
from utilities.file_manager.readers.txt_reader import TxtReader


class FileManager:

    @staticmethod
    def file_read(file: InMemoryUploadedFile):
        match file_type(file):
            case "application/zip":
                return DocxReader.read(file)
            case "application/pdf":
                return PdfReader.read(file)
            case "text/plain":
                return TxtReader.read(file)
