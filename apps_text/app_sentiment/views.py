from django.urls import reverse_lazy
from django.contrib import messages
from langdetect.lang_detect_exception import LangDetectException
from apps_text.app_sentiment.forms import SentimentForm
from apps_text.app_sentiment.tasks import sentiment_task
from utilities.base_text_lang.base_view import BaseTextFileExtraSaveResultView
from text_proc.sent_mod.sentiment_analyzer import SentimentAnalyzer
from text_proc.sent_mod.errors import SentimentAnalyzerError


class SentimentView(BaseTextFileExtraSaveResultView):
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

    def save_extra_hset(self, choose_input_text, processed_text, **kwargs):
        self.save_hset(
            input_text=choose_input_text,
            result=processed_text.classification,
            pos_per=processed_text.p_pos,
            neg_per=processed_text.p_neg,
            app_name=self.app_name,
            **kwargs,
        )

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        res = kwargs.get("res")
        kwargs.update(
            {
                "res": {
                    "Classification": res.classification,
                    "P_pos": res.p_pos,
                    "P_neg": res.p_neg,
                }
            }
        )
        return sentiment_task(
            user, task_model_pk, choose_input_text, method="sentiment", **kwargs
        )

    def setup_result(self, text):
        return self.get_method()(text)

    def get_method(self):
        return SentimentAnalyzer()
