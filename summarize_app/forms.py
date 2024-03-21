from django import forms
from utilities.base_text_lang.base_form import BaseTextProcMethodForm


class SummarizeForm(BaseTextProcMethodForm):
    num_sentences = forms.IntegerField(label='Количество предложений', min_value=10, max_value=100, initial=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Реферирование текста'
        self.fields['method'].label = 'Метод реферирования текста'
        self.fields['method'].choices = [('extractive', 'Extractive plus'), ('py_sum', 'PySum'), ]
