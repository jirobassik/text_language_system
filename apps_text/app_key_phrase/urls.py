from django.urls import path
from apps_text.app_key_phrase.views import KeyPhraseExtractionView
from apps_text.app_key_phrase.api import api

urlpatterns = [
    path("", KeyPhraseExtractionView.as_view(), name="key-phrase-view"),
    path("api/", api.urls),
]
