from django.views.generic import FormView

from utilities.file_manager.file import FileManager


class BaseTextProcView(FormView):
    button_name = ""

    def get_context_data(self, **kwargs):
        kwargs["button_name"] = self.button_name
        return super().get_context_data(**kwargs)

    def get_method(self):
        raise NotImplementedError(".get_methods() must be overridden")

    @staticmethod
    def choose_input(file, text):
        return FileManager.file_read(file) if file else text


class BaseTextFileView(BaseTextProcView):
    def form_valid(self, form):
        text, file = self.get_cleaned_text_file(form)
        context = self.setup_input_context(file, text)
        return self.render_to_response(context)

    def setup_input_context(self, file, text):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.get_method()(choose_input_text)
        return context

    @staticmethod
    def get_cleaned_text_file(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        return text, file


class BaseTextFileMethodView(BaseTextProcView):
    def form_valid(self, form):
        text, file, method = self.get_cleaned_text_file_method(form)
        context = self.setup_input_context(file, text, method)
        return self.render_to_response(context)

    def setup_input_context(self, file, text, method):
        choose_input_text = self.choose_input(file, text)
        context = self.get_context_data()
        context["result"] = self.get_method().get(method)(choose_input_text)
        return context

    @staticmethod
    def get_cleaned_text_file_method(form):
        text = form.cleaned_data.get("text")
        file = form.cleaned_data.get("file")
        method = form.cleaned_data.get("method")
        return text, file, method
