from django.views.generic import TemplateView


class TextLanguageView(TemplateView):
    template_name = "text_language/text_language.html"
