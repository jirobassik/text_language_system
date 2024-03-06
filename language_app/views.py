from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView
from django_htmx.http import HttpResponseClientRefresh

from language_app.forms import TextLanguageForm
from lang_mod.methods import methods
from utilities.file_manager.file import FileManager


class TextLanguageView(FormView):
    template_name = 'language_app/language_form.html'
    form_class = TextLanguageForm
    success_url = reverse_lazy('language_view')

    def form_valid(self, form):
        text = form.cleaned_data.get('text')
        method = form.cleaned_data.get('method')
        file = form.cleaned_data.get('file')
        print(method)
        choose_input_text = self.choose_input(file, text)
        if self.request.htmx:
            result_html = render_to_string('language_app/language_result.html',
                                           {'result': methods.get(method)(choose_input_text)})
            return HttpResponse(result_html)
        return super().form_valid(form)

    @staticmethod
    def choose_input(file, text):
        return FileManager.file_read(file) if file else text

    def form_invalid(self, form):
        return HttpResponseClientRefresh()
