from django.urls import path
from api_key.views import ApiKeyView, ApiKeyDeleteView

urlpatterns = [
    path("", ApiKeyView.as_view(), name="api-key-view"),
    path("delete/<int:pk>", ApiKeyDeleteView.as_view(), name="api-key-delete-view"),
]
