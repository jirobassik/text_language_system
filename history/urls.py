from django.urls import path
from history.views import HistoryListView, HistoryDetailView
from history.api import api

urlpatterns = [
    path("", HistoryListView.as_view(), name="history-list-view"),
    path("detail/<uuid:pk>", HistoryDetailView.as_view(), name="history-detail-view"),
    path("api/", api.urls),
]
