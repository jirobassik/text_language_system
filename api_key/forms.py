from django import forms
from api_key.models import ApiKeyModel


class ApiKeyForm(forms.ModelForm):
    class Meta:
        model = ApiKeyModel
        exclude = ("api_token", "created_at", "expired_at", "user")
