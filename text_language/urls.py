from django.urls import path
from text_language.views import main_view

urlpatterns = [
    path('', main_view, name='text_language'),
]
