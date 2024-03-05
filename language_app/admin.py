from django.contrib import admin
from language_app.models import LanguagePoaModel


@admin.register(LanguagePoaModel)
class LanguagePoaAdmin(admin.ModelAdmin):
    list_display = ['language', 'poa_snippet']
    search_fields = ['language']
    sortable_by = ['language']

    @admin.display(description="Name")
    def poa_snippet(self, obj):
        max_length = 50
        if len(obj.poa_text) > max_length:
            return f"{obj.poa_text[:max_length]}..."
        else:
            return f"{obj.poa_text}"

