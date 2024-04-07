from django.urls import path
from app_summarize.views import SummarizeView
from app_summarize.api import api

urlpatterns = [
    path("", SummarizeView.as_view(), name="summarize_view"),
    path("api/", api.urls),
]
