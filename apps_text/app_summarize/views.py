from django.urls import reverse_lazy

from apps_text.app_summarize.tasks import summarize_task
from utilities.base_text_lang.base_view import BaseTextFileExtraSaveResultView

from apps_text.app_summarize.forms import SummarizeForm
from text_proc.sum_mod.methods import methods
from utilities.base_text_lang.mixins import HsetMixin


class SummarizeView(BaseTextFileExtraSaveResultView, HsetMixin):
    template_name = "app_summarize/summarize_form.html"
    form_class = SummarizeForm
    success_url = reverse_lazy("summarize_view")
    button_name = "Реферировать текст"
    app_name = "app_summarize"

    def setup_result(self, text):
        return self.get_method().get(getattr(self, "method"))(
            text, getattr(self, "num_sentences")
        )

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        return summarize_task(user, task_model_pk, choose_input_text, **kwargs)

    def get_method(self):
        return methods
