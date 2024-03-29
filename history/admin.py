from django.contrib import admin

from history.models import HistoryModel


@admin.register(HistoryModel)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "input_text", "result_text", "user", "is_deleted", "created_at"]
    fields = ["input_text", "result_text", "user", "is_deleted"]
