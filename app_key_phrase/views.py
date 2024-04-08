import json

from django.contrib import messages
from django.urls import reverse_lazy
from langdetect.lang_detect_exception import LangDetectException

from utilities.base_text_lang.base_view import BaseTextProcView

from app_key_phrase.forms import KeyPhraseExtractionForm
from text_proc.key_phrase_mod.key_phrase_extractor import KeyPhraseExtractor
from utilities.base_text_lang.mixins import HsetMixin
from text_proc.key_phrase_mod.errors import KeyPhraseExtractorError


class KeyPhraseExtractionView(BaseTextProcView, HsetMixin):
    template_name = "app_key_phrase/key_phrase_form.html"
    form_class = KeyPhraseExtractionForm
    success_url = reverse_lazy("key-phrase-view")
    button_name = "Извлечь ключевые слов"
    app_name = "app_key_phrase"

    def form_valid(self, form):
        text, file, num_key_phrase = self.get_cleaned_text_file(form)
        context = self.setup_input_context(file, text, num_key_phrase)
        return self.render_to_response(context)

    def setup_input_context(self, file, text, num_key_phrase):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        try:
            context["result"] = self.gen_result(choose_input_text, num_key_phrase)
        except (KeyPhraseExtractorError, LangDetectException):
            messages.error(self.request, "Не удалось извлечь ключевые слова")
        return context

    def gen_result(self, choose_input_text, num_key_phrase):
        result = self.get_method()(choose_input_text, num_key_phrase)
        serialized_result = json.dumps(result, ensure_ascii=False)
        self.save_hset(
            input_text=choose_input_text,
            result=serialized_result,
            app_name=self.app_name,
        )
        return result

    @staticmethod
    def get_cleaned_text_file(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        num_key_phrase = form.cleaned_data.get("num_sentences")
        return text, file, num_key_phrase

    def get_method(self):
        return KeyPhraseExtractor()
