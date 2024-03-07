from django.db.models import TextChoices
from django.http import HttpResponse
from ninja import NinjaAPI, Schema, File
from ninja import UploadedFile
from ninja.errors import ValidationError

from lang_mod.methods import methods
from utilities.validators.api_file_validations import validate_api_file
from utilities.validators.text_validators import validate_api_text
from utilities.file_manager.file import FileManager

api = NinjaAPI()


class Methods(TextChoices):
    short = "short_word"
    langid = "langid"
    langdetect = "lang_detect"


class LanguageDet(Schema):
    text: str
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
