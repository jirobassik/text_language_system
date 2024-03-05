from django import forms


class TextLanguageForm(forms.Form):
    text = forms.CharField(max_length=1000, min_length=50, required=True, widget=forms.Textarea, initial='Hello world',
                           label='Текст')
    method = forms.ChoiceField(choices=[('short', 'Коротких слов'), ('langdetect', 'LangDetect'), ('langid', 'Langid')],
                               widget=forms.Select(attrs={'id': 'voice-select'}),
                               label='Метод определения языка', )
