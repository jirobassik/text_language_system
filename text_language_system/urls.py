"""
URL configuration for text_language_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("user_profile.urls"), name="account"),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("", include("text_language.urls")),
    path("json-download/", include("file_view.urls")),
    path("language-detector/", include("app_language.urls")),
    path("summarize-text/", include("app_summarize.urls")),
    path("classify-text/", include("app_classification.urls")),
    path("sentiment-text/", include("app_sentiment.urls")),
    path("extraction-entities-text/", include("app_extraction.urls")),
    path("api-key/", include("api_key.urls")),
    path("history/", include("history.urls")),
    path("status/", include("text_language_status.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
