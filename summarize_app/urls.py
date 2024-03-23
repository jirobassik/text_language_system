from django.urls import path
from summarize_app.views import SummarizeView
from summarize_app.api import api

urlpatterns = [
    path("", SummarizeView.as_view(), name="summarize_view"),
    path("api/", api.urls),
]
