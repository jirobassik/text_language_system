from django.urls import path
from app_classification.views import ClassifyView
from app_classification.api import api

urlpatterns = [
    path("", ClassifyView.as_view(), name="classification_view"),
    path("api/", api.urls),
]
