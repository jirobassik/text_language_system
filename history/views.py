from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from history.models import HistoryModel


class HistoryListView(LoginRequiredMixin, ListView):
    model = HistoryModel
    template_name = "history/history.html"
    context_object_name = "history_obj"

    def get_queryset(self):
        self.queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_queryset()


class HistoryDetailView(LoginRequiredMixin, DetailView):
    model = HistoryModel
    template_name = "history/history_detail.html"
    context_object_name = "history_detail_obj"

    def get_object(self, queryset=None):
        queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_object(queryset)
