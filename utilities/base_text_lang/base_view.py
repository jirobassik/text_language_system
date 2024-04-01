from django.views.generic import FormView
from django.contrib import messages
from utilities.file_manager.file import FileManager
from utilities.base_text_lang.mixins import HsetMixin

class BaseTextProcView(FormView, HsetMixin):
    button_name = ""
    app_name = ""

    def get_context_data(self, **kwargs):
        kwargs["button_name"] = self.button_name
        return super().get_context_data(**kwargs)

    def get_method(self):
        raise NotImplementedError(".get_methods() must be overridden")

    @staticmethod
    def choose_input(file, text):
        return FileManager().file_read(file) if file else text


class BaseTextFileView(BaseTextProcView):
    def form_valid(self, form):
        text, file = self.get_cleaned_text_file(form)
        context = self.setup_input_context(file, text)
        return self.render_to_response(context)

    def setup_input_context(self, file, text):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(choose_input_text)
        return context

    def gen_result(self, choose_input_text):
        result = self.get_method()(choose_input_text)
        self.set_hset(self.request.session.session_key, result=result, app_name=self.app_name)
        return result

    @staticmethod
    def get_cleaned_text_file(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        return text, file


class BaseTextFileMethodView(BaseTextProcView, HsetMixin):
    def form_valid(self, form):
        text, file, method = self.get_cleaned_text_file_method(form)
        context = self.setup_input_context(file, text, method)
        return self.render_to_response(context)

    def setup_input_context(self, file, text, method):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(method, choose_input_text)
        return context

    def gen_result(self, method, choose_input_text):
        try:
            result = self.get_method().get(method)(choose_input_text)
            self.set_hset(self.request.session.session_key, result=result, app_name=self.app_name)
            return result
        except ValueError:
            messages.error(self.request, "Не удалось обработать, свяжитесь с администратором")
            return False

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        return text, file, method
