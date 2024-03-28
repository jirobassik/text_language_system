from django.urls import path
from file_view.views import JsonView

urlpatterns = [
    path("download/", JsonView.as_view(), name="pdf_view"),
]
