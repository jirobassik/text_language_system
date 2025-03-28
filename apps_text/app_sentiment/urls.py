from django.urls import path
from apps_text.app_sentiment.views import SentimentView
from apps_text.app_sentiment.api import api

urlpatterns = [
    path("", SentimentView.as_view(), name="sentiment-view"),
    path("api/", api.urls),
]
