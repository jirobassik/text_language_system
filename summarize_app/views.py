from django.urls import reverse_lazy
from utilities.base_text_lang.base_view import BaseTextProcView

from summarize_app.forms import SummarizeForm
from text_proc.sum_mod.methods import methods


class SummarizeView(BaseTextProcView):
    template_name = 'summarize_app/summarize_form.html'
    form_class = SummarizeForm
    success_url = reverse_lazy('summarize_view')
    button_name = 'Реферировать текст'

    def form_valid(self, form):
        text, file, method, num_sentences = self.get_cleaned_text_file_method(form)
        context = self.setup_input_context(file, text, method, num_sentences)
        return self.render_to_response(context)

    def setup_input_context(self, file, text, method, num_sentences):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context['result'] = self.get_method().get(method)(choose_input_text, num_sentences)
        return context

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get('text')
        file = form.cleaned_data.get('file')
        method = form.cleaned_data.get('method')
        num_sentences = form.cleaned_data.get('num_sentences')
        return text, file, method, num_sentences

    def get_method(self):
        return methods
