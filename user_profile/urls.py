from django.urls import path, include

from user_profile.views import UpdateViewProfile

urlpatterns = [
    path("", include("django_registration.backends.activation.urls")),
    path("", include("django.contrib.auth.urls")),
    path("edit/", UpdateViewProfile.as_view(), name="edit"),
]
