from django import forms
from django.conf import settings
from utilities.validators.file_validations import content_validation, max_size_validation, extension_validation, \
    max_length_file_text, min_length_file_text


class BaseTextProcForm(forms.Form):
    initial_text = 'I arrived during the first week of September. The weather has been very nice. Even though it\'s ' \
                   'October, it\'s still rather sunny and warm. In fact, I went to the beach and swam in the ' \
                   'Mediterranean Sea earlier today. I am living with a very welcoming host family.'

    text = forms.CharField(
        max_length=settings.VALID_MAX_FORM_LENGTH_TEXT,
        min_length=settings.VALID_MIN_FORM_LENGTH_TEXT,
        required=False,
        widget=forms.Textarea(attrs={'class': 'text-input'}),
        initial=initial_text,
        label=f'Введите текст или выберите файл для обработки',
        help_text=f'Текст длиной от {settings.VALID_MIN_FORM_LENGTH_TEXT} до '
                  f'{settings.VALID_MAX_FORM_LENGTH_TEXT} символов',
    )

    file = forms.FileField(
        required=False,
        label='Файл',
        validators=(extension_validation, content_validation, max_size_validation),
        widget=forms.ClearableFileInput(attrs={'class': 'file-input'}),
        help_text='Файл размера не больше 2 МБ и формата: DOCX, PDF, TXT'
    )

    def clean_file(self):
        cd = self.cleaned_data.get('file')
        if cd:
            for validator in (min_length_file_text, max_length_file_text):
                validator(cd)
        return cd


class BaseTextProcMethodForm(BaseTextProcForm):
    method = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'method-select'}),
    )
