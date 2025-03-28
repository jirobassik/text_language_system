from django.contrib.auth.mixins import AccessMixin
from django.views.generic import FormView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from overrides import override

from utilities.base_text_lang.base_status import BaseStatusImmediately
from utilities.file_manager.file import FileManager
from utilities.base_text_lang.mixins import HsetMixin


class BaseTextProcView(FormView, HsetMixin):
    button_name = ""
    app_name = ""

    def get_context_data(self, **kwargs):
        kwargs["button_name"] = self.button_name
        return super().get_context_data(**kwargs)

    def get_method(self):
        raise NotImplementedError(".get_method() must be overridden")

    def save_hset(self, **kwargs):
        try:
            self.set_hset(self.request.session.session_key, **kwargs)
        except ValueError:
            messages.error(
                self.request, "Не удалось обработать, свяжитесь с администратором"
            )

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
        self.save_hset(
            input_text=choose_input_text,
            result=result,
            app_name=self.app_name,
        )
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
        result = self.get_method().get(method)(choose_input_text)
        self.save_hset(
            input_text=choose_input_text,
            result=result,
            method=method,
            app_name=self.app_name,
        )
        return result

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        return text, file, method


class BaseTextFileMethodCheckBoxView(
    BaseTextProcView, BaseStatusImmediately, AccessMixin
):
    def form_valid(self, form):
        text, file, method, checkbox = self.get_cleaned_text_file_method(form)
        try:
            context = self.setup_input_context(file, text, method, checkbox)
            return self.render_to_response(context)
        except PermissionDenied:
            return self.handle_no_permission()

    def setup_input_context(self, file, text, method, checkbox):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(method, choose_input_text, checkbox)
        return context

    @override(check_signature=False)
    def gen_result(self, method, choose_input_text, checkbox):
        result = self.get_method().get(method)(choose_input_text)
        self.save_hset(
            input_text=choose_input_text,
            result=result,
            method=method,
            app_name=self.app_name,
        )
        return self.check_user_checkbox(checkbox, choose_input_text, result)

    def check_user_checkbox(self, checkbox, choose_input_text, result):
        if checkbox and not self.request.user.is_authenticated:
            raise PermissionDenied
        elif checkbox and self.request.user.is_authenticated:
            super().gen_result(choose_input_text, res=result)
            return result
        else:
            return result

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        checkbox = form.cleaned_data.get("checkbox")
        return text, file, method, checkbox
