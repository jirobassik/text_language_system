from django import forms
from utilities.base_text_lang.base_form import BaseTextProcForm


class KeyPhraseExtractionForm(BaseTextProcForm):
    num_sentences = forms.IntegerField(
        label="Количество ключевых слов", min_value=5, max_value=50, initial=5
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Извлечение ключевых слов"
