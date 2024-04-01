from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from text_language_status.models import TextLanguageManagerModel


class StatusListView(LoginRequiredMixin, ListView):
    model = TextLanguageManagerModel
    template_name = "text_language_status/text_language_status.html"
    context_object_name = "status_obj"

    def get_queryset(self):
        self.queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_queryset()
