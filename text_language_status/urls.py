from django.urls import path
from text_language_status.views import StatusListView

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list-view"),
]
