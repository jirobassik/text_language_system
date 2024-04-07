from django.urls import path
from app_language.views import TextLanguageView
from app_language.api import api


urlpatterns = [
    path("", TextLanguageView.as_view(), name="language_view"),
    path("api/", api.urls),
]
