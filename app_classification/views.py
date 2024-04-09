import json

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View

from utilities.base_text_lang.base_status import BaseStatus
from utilities.base_text_lang.base_view import BaseTextFileView
from utilities.redis_com.errors import MaxLongOperationsError

from app_classification.forms import ClassifyForm
from app_classification.tasks import classify_long_task
from text_proc.clas_mod.neuro_classification import NeuroTextClassifier
from utilities.server_request.error import SendError

class ClassifyView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return ClassifyAuthView.as_view()(request, *args, **kwargs)
        else:
            return ClassifyNotAuthView.as_view()(request, *args, **kwargs)


class ClassifyNotAuthView(BaseTextFileView):
    template_name = "app_classification/classification_form.html"
    form_class = ClassifyForm
    success_url = reverse_lazy("classification_view")
    button_name = "Классифицировать текст"
    app_name = "app_classification"

    def form_valid(self, form):
        text, file, method, num_sentences = self.get_cleaned_text_file_method(form)
        context = self.setup_input_context(file, text)
        return self.render_to_response(context)

    def setup_input_context(self, file, text):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(choose_input_text)
        return context

    def gen_result(self, choose_input_text):
        try:
            result = self.get_method()(choose_input_text)
            serialized_data = json.dumps(
                result,
                default=list,
                ensure_ascii=False,
            )
            self.set_hset(
                self.request.session.session_key,
                input_text=choose_input_text,
                result=serialized_data,
                app_name=self.app_name,
            )
            return result
        except SendError:
            messages.error(self.request, "Не удалось обработать, свяжитесь с администратором")
            return False

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        num_sentences = form.cleaned_data.get("num_sentences")
        return text, file, method, num_sentences

    def get_method(self):
        return NeuroTextClassifier()


class ClassifyAuthView(BaseStatus, ClassifyNotAuthView):

    def form_valid(self, form):
        text, file, method, num_sentences = self.get_cleaned_text_file_method(form)
        self.setup_input_context(file, text)
        return HttpResponseRedirect(self.get_success_url())

    def setup_input_context(self, file, text):
        try:
            choose_input_text = self.choose_input(file, text)
            self.gen_result(choose_input_text)
            messages.success(
                self.request,
                "Задача добавлена в очередь на выполнение. Результат можно увидеть в 'Истории'",
            )
        except MaxLongOperationsError:
            messages.warning(self.request, "Превышен лимит максимального числа задач")

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        return classify_long_task(user, task_model_pk, choose_input_text, **kwargs)
