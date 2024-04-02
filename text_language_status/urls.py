from django.urls import path
from text_language_status.views import StatusListView, revoke_task

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list-view"),
    path("revoke/<uuid:task_id>", revoke_task, name="revoke-task"),
]
