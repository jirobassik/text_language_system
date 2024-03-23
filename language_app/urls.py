from django.urls import path
from language_app.views import TextLanguageView
from language_app.api import api

urlpatterns = [
    path("", TextLanguageView.as_view(), name="language_view"),
    path("api/", api.urls),
]
