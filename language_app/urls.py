from django.urls import path
from language_app.views import TextLanguageView
from language_app.api import api
from file_view.urls import urlpatterns as file_url

urlpatterns = [
    path("", TextLanguageView.as_view(), name="language_view"),
    path("api/", api.urls),
] + file_url
