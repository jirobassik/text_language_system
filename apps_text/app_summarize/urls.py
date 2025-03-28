from django.urls import path
from apps_text.app_summarize.views import SummarizeView
from apps_text.app_summarize.api import api

urlpatterns = [
    path("", SummarizeView.as_view(), name="summarize_view"),
    path("api/", api.urls),
]
