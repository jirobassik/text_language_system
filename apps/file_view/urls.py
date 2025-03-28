from django.urls import path
from apps.file_view.views import JsonView

urlpatterns = [
    path("", JsonView.as_view(), name="json_view"),
]
