from django.urls import path
from api_key.views import ApiKeyView

urlpatterns = [
    path("", ApiKeyView.as_view(), name="api-key-view"),
]
