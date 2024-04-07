from utilities.base_text_lang.base_form import BaseTextProcMethodForm


class TextLanguageForm(BaseTextProcMethodForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Определение языка"
        self.fields["method"].label = "Метод определения языка"
        self.fields["method"].choices = [
            ("short", "Коротких слов"),
            ("langdetect", "LangDetect"),
            ("langid", "Langid"),
        ]
