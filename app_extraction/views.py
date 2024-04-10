from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException
from app_extraction.forms import ExtractionForm
from utilities.base_text_lang.base_view import BaseTextFileView
from text_proc.ent_mod.entity_extraction import EntityExtraction
from text_proc.ent_mod.errors import EntityExtractionError
from utilities.converter import convert_to_serializable

class ExtractionView(BaseTextFileView):
    template_name = "app_extraction/extraction_form.html"
    form_class = ExtractionForm
    success_url = reverse_lazy("extraction-view")
    button_name = "Извлечь именованные сущности"
    app_name = "app_extraction"

    def setup_input_context(self, file, text):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        try:
            context["result"] = self.gen_result(choose_input_text)
        except (LangDetectException, EntityExtractionError):
            messages.error(self.request, "Не удалось извлечь именованные сущности")
        return context

    def gen_result(self, choose_input_text):
        result = self.get_method()(choose_input_text)
        self.save_hset(
            result=convert_to_serializable(result, default=list),
            input_text=choose_input_text,
            app_name=self.app_name,
        )
        return result

    def get_method(self):
        return EntityExtraction()
