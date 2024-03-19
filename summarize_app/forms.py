from utilities.base_text_lang.base_form import BaseTextProcMethodForm


class SummarizeForm(BaseTextProcMethodForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Реферирование текста'
        self.fields['method'].label = 'Метод реферирования текста'
        self.fields['method'].choices = [('extractive', 'Extractive plus'), ('py_sum', 'PySum'), ]
