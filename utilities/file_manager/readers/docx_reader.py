import docx


class DocxReader:

    @staticmethod
    def read(file):
        doc = docx.Document(file)
        text_content = []

        for paragraph in doc.paragraphs:
            text_content.append(paragraph.text)
        text = "\n".join(text_content)
        print("docx", text)
        return text
