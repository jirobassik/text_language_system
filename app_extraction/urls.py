from django.urls import path
from app_extraction.views import ExtractionView
from app_extraction.api import api

urlpatterns = [
    path("", ExtractionView.as_view(), name="extraction-view"),
    path("api/", api.urls)
]
