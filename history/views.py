from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from history.models import HistoryModel
from utilities.base_text_lang.mixins import HsetMixin


class HistoryListView(LoginRequiredMixin, ListView):
    model = HistoryModel
    template_name = "history/history.html"
    context_object_name = "history_obj"

    def get_queryset(self):
        self.queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_queryset()


class HistoryDetailView(LoginRequiredMixin, DetailView, HsetMixin):
    model = HistoryModel
    template_name = "history/history_detail.html"
    context_object_name = "history_detail_obj"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.set_hset(
            self.request.session.session_key,
            expire_time=400,
            input_text=self.object.input_text,
            result=self.object.result_text,
        )
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        queryset = self.model.objects.filter(user=self.request.user, is_deleted=False)
        return super().get_object(queryset)
