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
                  path('admin/', admin.site.urls),
                  path('account/', include('user_profile.urls'), name='account'),
                  path('social-auth/',
                       include('social_django.urls', namespace='social')),
                  path('', include('text_language.urls')),
                  path('language-detector/', include('language_app.urls')),
                  path('api-key/', include('api_key.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
