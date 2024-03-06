from django import forms
from utilities.file_manager.file_validations import content_validation, max_size_validation, extension_validation


class TextLanguageForm(forms.Form):
    text = forms.CharField(max_length=1000, min_length=50, required=False, widget=forms.Textarea, initial='Hello world',
                           label='Текст')
    method = forms.ChoiceField(choices=[('short', 'Коротких слов'), ('langdetect', 'LangDetect'), ('langid', 'Langid')],
                               widget=forms.Select(attrs={'id': 'voice-select'}),
                               label='Метод определения языка', )
    file = forms.FileField(required=False, label='Файл',
                           validators=(content_validation, max_size_validation, extension_validation))
