from django.urls import path
from language_app.views import TextLanguageView

urlpatterns = [
    path('', TextLanguageView.as_view(), name='language_view')
]
