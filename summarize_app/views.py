from django.urls import reverse_lazy
from utilities.base_text_lang.base_view import BaseTextFileMethodView

from summarize_app.forms import SummarizeForm
from text_proc.sum_mod.methods import methods


class SummarizeView(BaseTextFileMethodView):
    template_name = 'summarize_app/summarize_form.html'
    form_class = SummarizeForm
    success_url = reverse_lazy('summarize_view')
    button_name = 'Реферировать текст'

    def get_method(self):
        return methods
