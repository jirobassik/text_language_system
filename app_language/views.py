from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException

from utilities.base_text_lang.base_view import BaseTextFileMethodView

from app_language.forms import TextLanguageForm
from text_proc.lang_mod.methods import methods


class TextLanguageView(BaseTextFileMethodView):
    template_name = "app_language/language_form.html"
    form_class = TextLanguageForm
    success_url = reverse_lazy("language_view")
    button_name = "Определить язык"
    app_name = "app_language"

    def setup_input_context(self, file, text, method):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        try:
            context["result"] = self.gen_result(method, choose_input_text)
        except LangDetectException:
            messages.error(self.request, "Не удалось определить язык")
        return context

    def get_method(self):
        return methods
