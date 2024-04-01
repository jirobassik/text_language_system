from django.urls import reverse_lazy
from utilities.base_text_lang.base_view import BaseTextFileMethodView

from language_app.forms import TextLanguageForm
from text_proc.lang_mod.methods import methods


class TextLanguageView(BaseTextFileMethodView):
    template_name = "language_app/language_form.html"
    form_class = TextLanguageForm
    success_url = reverse_lazy("language_view")
    button_name = "Определить язык"
    app_name = "language_app"

    def get_method(self):
        return methods
