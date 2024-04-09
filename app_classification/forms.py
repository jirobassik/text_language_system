from utilities.base_text_lang.base_form import BaseTextProcForm


class ClassifyForm(BaseTextProcForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Классификация текста"
