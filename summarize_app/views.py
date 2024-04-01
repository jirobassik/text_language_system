from django.urls import reverse_lazy
from utilities.base_text_lang.base_view import BaseTextProcView

from summarize_app.forms import SummarizeForm
from text_proc.sum_mod.methods import methods
from utilities.base_text_lang.mixins import HsetMixin


class SummarizeView(BaseTextProcView, HsetMixin):
    template_name = "summarize_app/summarize_form.html"
    form_class = SummarizeForm
    success_url = reverse_lazy("summarize_view")
    button_name = "Реферировать текст"
    app_name = "summarize_app"

    def form_valid(self, form):
        text, file, method, num_sentences = self.get_cleaned_text_file_method(form)
        context = self.setup_input_context(file, text, method, num_sentences)
        return self.render_to_response(context)

    def setup_input_context(self, file, text, method, num_sentences):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(method, choose_input_text, num_sentences)
        return context

    def gen_result(self, method, choose_input_text, num_sentences):
        result = self.get_method().get(method)(choose_input_text, num_sentences)
        self.set_hset(self.request.session.session_key, result=result, app_name=self.app_name)
        return result

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        num_sentences = form.cleaned_data.get("num_sentences")
        return text, file, method, num_sentences

    def get_method(self):
        return methods
