from django.urls import path
from apps_text.text_language.views import TextLanguageView

urlpatterns = [
    path("", TextLanguageView.as_view(), name="text_language"),
]
