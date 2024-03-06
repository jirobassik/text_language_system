import PyPDF2
from django.core.files.uploadedfile import InMemoryUploadedFile


class PdfReader:

    @staticmethod
    def read(file: InMemoryUploadedFile):
        text = ''
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
        print('pdf', text)
        return text
