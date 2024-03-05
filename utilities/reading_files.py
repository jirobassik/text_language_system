from pathlib import Path

import PyPDF2


class ReadFile:

    @staticmethod
    def reading_txt_file(filename: str):
        return Path("../media", filename).read_text('utf-8')

    @staticmethod
    def reading_pdf_file(folder_name: str, filename: str):
        text = ""
        with open(Path(f'../{folder_name}', filename), 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
