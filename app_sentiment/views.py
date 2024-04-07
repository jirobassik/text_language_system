from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException
from app_sentiment.forms import SentimentForm
from utilities.base_text_lang.base_view import BaseTextFileView
from text_proc.sent_mod.sentiment_analyzer import SentimentAnalyzer
from text_proc.sent_mod.errors import SentimentAnalyzerError

class SentimentView(BaseTextFileView):
    template_name = "app_sentiment/sentiment_form.html"
    form_class = SentimentForm
    success_url = reverse_lazy("sentiment-view")
    button_name = "Определить тональность"
    app_name = "app_sentiment"

    def setup_input_context(self, file, text):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        try:
            context["result"] = self.gen_result(choose_input_text)
        except (SentimentAnalyzerError, LangDetectException):
            messages.error(self.request, "Не удалось определить тональность")
        return context

    def get_method(self):
        return SentimentAnalyzer()
