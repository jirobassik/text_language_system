from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException

from apps_text.app_language.tasks import language_task
from utilities.base_text_lang.base_view import BaseTextFileExtraSaveResultView

from apps_text.app_language.forms import TextLanguageForm
from text_proc.lang_mod.methods import methods


class TextLanguageView(BaseTextFileExtraSaveResultView):
    template_name = "app_language/language_form.html"
    form_class = TextLanguageForm
    success_url = reverse_lazy("language_view")
    button_name = "Определить язык"
    app_name = "app_language"

    def setup_input_context(self, file, text, **kwargs):
        try:
            context = super().setup_input_context(file, text, **kwargs)
            return context
        except (LangDetectException, ValueError):
            messages.error(self.request, "Не удалось определить язык")
        return self.get_context_data()

    def setup_result(self, text):
        return self.get_method().get(getattr(self, "method"))(text)

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        return language_task(
            user,
            task_model_pk,
            choose_input_text,
            method=getattr(self, "method"),
            **kwargs
        )

    def get_method(self):
        return methods
