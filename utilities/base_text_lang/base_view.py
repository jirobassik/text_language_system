from django.contrib.auth.mixins import AccessMixin
from django.views.generic import FormView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from utilities.base_text_lang.base_status import BaseStatusImmediately
from utilities.converter import convert_to_serializable
from utilities.file_manager.file import FileManager
from utilities.base_text_lang.mixins import HsetMixin


class BaseTextProcView(FormView, HsetMixin):
    button_name = ""
    app_name = ""

    def get_context_data(self, **kwargs):
        kwargs["button_name"] = self.button_name
        return super().get_context_data(**kwargs)

    @staticmethod
    def choose_input(file, text):
        return FileManager().file_read(file) if file else text

    def save_hset(self, **kwargs):
        kwargs.pop("checkbox", "")
        try:
            self.set_hset(self.request.session.session_key, **kwargs)
        except ValueError:
            messages.error(
                self.request, "Не удалось обработать, свяжитесь с администратором"
            )

    def setup_input_context(self, file, text, **kwargs):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.gen_result(choose_input_text, **kwargs)
        return context

    def get_method(self):
        raise NotImplementedError(".get_method() must be overridden")

    def gen_result(self, choose_input_text, **kwargs):
        raise NotImplementedError(".gen_result() must be overridden")


class BaseTextFileExtraView(BaseTextProcView, HsetMixin):
    valid_extra_data = ["method", "num_sentences", "checkbox", "num_key_phrase"]
    preprocess_result: bool = False
    preprocess_result_extra_value: dict = {}

    def form_valid(self, form):
        text, file = form.cleaned_data.pop("text"), form.cleaned_data.pop("file")
        extra_kwargs = form.cleaned_data
        self.setup_extra_kwargs(**extra_kwargs)
        context = self.setup_input_context(file, text, **extra_kwargs)
        return self.render_to_response(context)

    def setup_extra_kwargs(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.valid_extra_data:
                setattr(self, key, value)

    def gen_result(self, choose_input_text, **kwargs):
        processed_text = self.setup_result(choose_input_text)
        self.save_extra_hset(choose_input_text, processed_text, **kwargs)
        return processed_text

    def save_extra_hset(self, choose_input_text, processed_text, **kwargs):
        self.save_hset(
            input_text=choose_input_text,
            result=(
                processed_text
                if not self.preprocess_result
                else convert_to_serializable(processed_text, **self.preprocess_result_extra_value)
            ),
            app_name=self.app_name,
            **kwargs,
        )

    def setup_result(self, text):
        raise NotImplementedError(".setup_result() must be overridden")


class BaseTextFileExtraSaveResultView(
    BaseTextFileExtraView, BaseStatusImmediately, AccessMixin
):
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except PermissionDenied:
            return self.handle_no_permission()

    def gen_result(self, choose_input_text, **kwargs):
        result = super().gen_result(choose_input_text, **kwargs)
        return self.check_user_checkbox(
            getattr(self, "checkbox"), choose_input_text, result
        )

    def check_user_checkbox(self, checkbox, choose_input_text, result):
        if checkbox and not self.request.user.is_authenticated:
            raise PermissionDenied
        elif checkbox and self.request.user.is_authenticated:
            super(BaseStatusImmediately, self).gen_result(choose_input_text, res=result)
            return result
        else:
            return result
