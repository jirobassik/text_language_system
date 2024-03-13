from django.urls import reverse_lazy
from django.views.generic import FormView

from language_app.forms import TextLanguageForm
from text_proc.lang_mod.methods import methods
from utilities.file_manager.file import FileManager


class TextLanguageView(FormView):
    template_name = 'language_app/language_form.html'
    form_class = TextLanguageForm
    success_url = reverse_lazy('language_view')

    def form_valid(self, form):
        text = form.cleaned_data.get('text')
        method = form.cleaned_data.get('method')
        file = form.cleaned_data.get('file')
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context['result'] = methods.get(method)(choose_input_text)
        return self.render_to_response(context)

    @staticmethod
    def choose_input(file, text):
        return FileManager.file_read(file) if file else text
