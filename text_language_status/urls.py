from django.urls import path
from text_language_status.views import StatusListView, RevokeTaskView
from text_language_status.api import api

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list-view"),
    path("revoke/<uuid:task_id>", RevokeTaskView.as_view(), name="revoke"),
    path("api/", api.urls),
]
