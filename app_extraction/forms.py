from utilities.base_text_lang.base_form import BaseTextProcForm


class ExtractionForm(BaseTextProcForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Извлечение именованных сущностей"
