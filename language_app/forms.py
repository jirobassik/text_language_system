from django import forms
from utilities.validators.file_validations import content_validation, max_size_validation, extension_validation


class TextLanguageForm(forms.Form):
    initial_text = 'I arrived during the first week of September. The weather has been very nice. Even though it\'s ' \
                   'October, it\'s still rather sunny and warm. In fact, I went to the beach and swam in the ' \
                   'Mediterranean Sea earlier today. I am living with a very welcoming host family.'

    text = forms.CharField(
        max_length=1000,
        min_length=50,
        required=False,
        widget=forms.Textarea(attrs={'class': 'text-input'}),
        initial=initial_text,
        label='Определения языка. Введите текст или выберите файл для обработки',
        help_text='Текст длиной от 50 до 1000 символов',
    )

    file = forms.FileField(
        required=False,
        label='Файл',
        validators=(content_validation, max_size_validation, extension_validation),
        widget=forms.ClearableFileInput(attrs={'class': 'file-input'}),
        help_text='Файл размера не больше 30 KБ и формата: DOCX, PDF, TXT'
    )

    method = forms.ChoiceField(
        choices=[('short', 'Коротких слов'), ('langdetect', 'LangDetect'), ('langid', 'Langid')],
        widget=forms.Select(attrs={'class': 'method-select'}),
        label='Метод определения языка'
    )
