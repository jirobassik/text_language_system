from django.urls import path
from apps.file_view.views import JsonView, TxtView

urlpatterns = [
    path("json/", JsonView.as_view(), name="json_view"),
    path("txt/", TxtView.as_view(), name="txt_view"),
]
