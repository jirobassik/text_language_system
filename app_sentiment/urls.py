from django.urls import path
from app_sentiment.views import SentimentView
from app_sentiment.api import api

urlpatterns = [
    path("", SentimentView.as_view(), name="sentiment-view"),
    path("api/", api.urls)
]
