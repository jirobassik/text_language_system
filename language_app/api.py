from django.db.models import TextChoices
from django.http import HttpResponse
from ninja import NinjaAPI, Schema, File
from ninja import UploadedFile
from ninja.errors import ValidationError

from text_proc.lang_mod.methods import methods
from utilities.api.auth import ApiKey
from utilities.validators.api_file_validations import validate_api_file
from utilities.validators.api_text_validators import validate_api_text
from utilities.file_manager.file import FileManager

api = NinjaAPI(auth=ApiKey(), title="Language detector API",
               description='<p>API для определения '
                           'языка.<br><b>Ограничения</b><br>Текст: от 50 до 1000 символов<br>Файл: от 50 до 3500 '
                           'символов. Расширения: DOCX, PDF, TXT. Размер не более 2 мб</p>')

initial_text = '''I am living with a very welcoming host family. I have my own private bedroom, but we eat breakfast.'''


class Methods(TextChoices):
    short = "short_word"
    langid = "langid"
    langdetect = "lang_detect"


class LanguageDet(Schema):
    text: str = initial_text
    method: Methods = 'short_word'


class LanguageDetFile(Schema):
    method: Methods = 'short_word'


@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    return HttpResponse(exc, status=422)


@api.post("/")
def lang_detect_api_text(request, lang_text_schem: LanguageDet):
    validate_api_text(lang_text_schem.text)
    res = methods.get(lang_text_schem.method.name)(lang_text_schem.text)
    return {"result": res}


@api.post("/file")
def lang_detect_api_file(request, method: LanguageDetFile, file: UploadedFile = File(...)):
    validate_api_file(file)
    res = methods.get(method.method.name)(FileManager.file_read(file))
    return {"result": res}
