from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException
from apps_text.app_extraction.forms import ExtractionForm
from apps_text.app_extraction.tasks import extraction_task
from utilities.base_text_lang.base_view import BaseTextFileExtraSaveResultView
from text_proc.ent_mod.entity_extraction import EntityExtraction
from text_proc.ent_mod.errors import EntityExtractionError


class ExtractionView(BaseTextFileExtraSaveResultView):
    template_name = "app_extraction/extraction_form.html"
    form_class = ExtractionForm
    success_url = reverse_lazy("extraction-view")
    button_name = "Извлечь именованные сущности"
    app_name = "app_extraction"
    preprocess_result = True
    preprocess_result_extra_value = {"default": list}

    def setup_input_context(self, file, text, **kwargs):
        try:
            context = super().setup_input_context(file, text, **kwargs)
            return context
        except (LangDetectException, EntityExtractionError):
            messages.error(self.request, "Не удалось извлечь именованные сущности")
        return self.get_context_data()

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        return extraction_task(user, task_model_pk, choose_input_text, **kwargs)

    def setup_result(self, text):
        return self.get_method()(text)

    def get_method(self):
        return EntityExtraction()
