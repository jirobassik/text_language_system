from utilities.base_text_lang.base_form import BaseTextProcForm


class SentimentForm(BaseTextProcForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Определение тональности"
