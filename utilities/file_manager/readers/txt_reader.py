from django.core.files.uploadedfile import InMemoryUploadedFile


class TxtReader:

    @staticmethod
    def read(file: InMemoryUploadedFile):
        text = file.read().decode("utf-8")
        return text
