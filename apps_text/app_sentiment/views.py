from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException
from apps_text.app_sentiment.forms import SentimentForm
from utilities.base_text_lang.base_view import BaseTextFileView
from text_proc.sent_mod.sentiment_analyzer import SentimentAnalyzer
from text_proc.sent_mod.errors import SentimentAnalyzerError


class SentimentView(BaseTextFileView):
    template_name = "app_sentiment/sentiment_form.html"
    form_class = SentimentForm
    success_url = reverse_lazy("sentiment-view")
    button_name = "Определить тональность"
    app_name = "app_sentiment"

    def setup_input_context(self, file, text, **kwargs):
        try:
            context = super().setup_input_context(file, text, **kwargs)
            return context
        except (SentimentAnalyzerError, LangDetectException):
            messages.error(self.request, "Не удалось определить тональность")
        return self.get_context_data()

    def gen_result(self, choose_input_text, **kwargs):
        result = self.get_method()(choose_input_text)
        self.save_hset(
            input_text=choose_input_text,
            result=result.classification,
            pos_per=result.p_pos,
            neg_per=result.p_neg,
            app_name=self.app_name,
        )
        return result

    def get_method(self):
        return SentimentAnalyzer()
