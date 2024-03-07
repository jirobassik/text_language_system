from django import forms
from utilities.validators.file_validations import content_validation, max_size_validation, extension_validation


class TextLanguageForm(forms.Form):
    initial_text = '''I arrived during the first week of September. The weather has been very nice. Even though it's 
    October, it's still rather sunny and warm. In fact, I went to the beach and swam in the Mediterranean Sea earlier 
    today. I am living with a very welcoming host family.'''

    text = forms.CharField(max_length=1000, min_length=50, required=False, widget=forms.Textarea, initial=initial_text,
                           label='Текст')
    method = forms.ChoiceField(choices=[('short', 'Коротких слов'), ('langdetect', 'LangDetect'), ('langid', 'Langid')],
                               widget=forms.Select(attrs={'id': 'voice-select'}),
                               label='Метод определения языка', )
    file = forms.FileField(required=False, label='Файл',
                           validators=(content_validation, max_size_validation, extension_validation))
