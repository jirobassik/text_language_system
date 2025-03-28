from django.urls import path
from apps_text.app_classification.views import ClassifyView
from apps_text.app_classification.api import api

urlpatterns = [
    path("", ClassifyView.as_view(), name="classification_view"),
    path("api/", api.urls),
]
