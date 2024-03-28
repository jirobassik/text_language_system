from django.urls import path
from summarize_app.views import SummarizeView
from summarize_app.api import api
from file_view.urls import urlpatterns as file_url

urlpatterns = [
    path("", SummarizeView.as_view(), name="summarize_view"),
    path("api/", api.urls),
] + file_url
