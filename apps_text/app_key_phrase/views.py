from django.contrib import messages
from django.urls import reverse_lazy
from langdetect.lang_detect_exception import LangDetectException
from apps_text.app_key_phrase.tasks import key_phrase_task
from utilities.base_text_lang.base_view import BaseTextFileExtraSaveResultView
from apps_text.app_key_phrase.forms import KeyPhraseExtractionForm
from text_proc.key_phrase_mod.key_phrase_extractor import KeyPhraseExtractor
from utilities.base_text_lang.mixins import HsetMixin
from text_proc.key_phrase_mod.errors import KeyPhraseExtractorError
from utilities.converter import convert_to_serializable


class KeyPhraseExtractionView(BaseTextFileExtraSaveResultView, HsetMixin):
    template_name = "app_key_phrase/key_phrase_form.html"
    form_class = KeyPhraseExtractionForm
    success_url = reverse_lazy("key-phrase-view")
    button_name = "Извлечь ключевые слова"
    app_name = "app_key_phrase"
    preprocess_result = True

    def setup_input_context(self, file, text, **kwargs):
        try:
            context = super().setup_input_context(file, text, **kwargs)
            return context
        except (KeyPhraseExtractorError, LangDetectException):
            messages.error(self.request, "Не удалось извлечь ключевые слова")
        return self.get_context_data()

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        kwargs.update({"res": convert_to_serializable(kwargs.get("res"))})
        return key_phrase_task(user, task_model_pk, choose_input_text, **kwargs)

    def setup_result(self, text):
        return self.get_method()(text, getattr(self, "num_key_phrase"))

    def get_method(self):
        return KeyPhraseExtractor()
