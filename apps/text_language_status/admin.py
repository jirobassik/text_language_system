from django.contrib import admin

from apps.text_language_status.models import TextLanguageManagerModel


@admin.register(TextLanguageManagerModel)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "task_id", "status", "text", "time_add", "user", "is_deleted"]
