from django.urls import path
from text_language_status.views import StatusListView
from text_language_status.api import api

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list-view"),
    path("api/", api.urls),
]
