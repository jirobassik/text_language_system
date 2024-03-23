from django.contrib import admin
from api_key.models import ApiKeyModel


@admin.register(ApiKeyModel)
class ApiTokenAdmin(admin.ModelAdmin):
    list_display = [
        "api_token",
        "created_at",
        "expired_at",
        "is_deleted",
        "is_expired",
        "user",
    ]
