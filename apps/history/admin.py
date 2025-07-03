from django.contrib import admin

from apps.history.models import HistoryModel


@admin.register(HistoryModel)
class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "input_text",
        "result_text",
        "method",
        "user",
        "is_deleted",
        "created_at",
    ]
    fields = ["input_text", "result_text", "method", "user", "is_deleted"]
