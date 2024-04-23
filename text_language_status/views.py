from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, RedirectView

from text_language_status.models import TextLanguageManagerModel
from utilities.task.revoke_task import revoke_task

class StatusListView(LoginRequiredMixin, ListView):
    model = TextLanguageManagerModel
    template_name = "text_language_status/text_language_status.html"
    context_object_name = "status_obj"

    def get_queryset(self):
        self.queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        if self.request.htmx:
            self.template_name = "text_language_status/status_table.html"
        return super().get(request)


class RevokeTaskView(LoginRequiredMixin, RedirectView):
    query_string = True
    permanent = True
    pattern_name = "status-list-view"

    def get_redirect_url(self, *args, **kwargs):
        task_id = kwargs["task_id"]
        revoke_task(task_id, self.request.user)
        return super().get_redirect_url()
