from django.db.models import TextChoices
from django.http import HttpResponse
from ninja import Schema, File
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from text_proc.sum_mod.methods import methods
from utilities.api.auth import ApiKey
from utilities.api.setup_throttle import User60MinRateThrottle, User100PerDayRateThrottle
from utilities.validators.api_file_validations import validate_api_file
from utilities.validators.api_text_validators import validate_api_text
from utilities.file_manager.file import FileManager
from ninja_extra.throttling import throttle

api = NinjaExtraAPI(auth=ApiKey(), title="Summarize text API", urls_namespace='summarize_api',
                    description='<p>API для реферирования текста. '
                                '<br><b>Ограничения</b><br>Текст: от 50 до 1000 символов<br>Файл: от 50 до 3500 '
                                'символов. Расширения: DOCX, PDF, TXT. Размер не более 2 мб<br>'
                                'Запросы: 60 в минуту и 100 в день</p>')


@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    return HttpResponse(exc, status=422)


initial_text = '''I am living with a very welcoming host family. I have my own private bedroom, but we eat breakfast, 
lunch, and dinner together. On Sundays, we eat a big home-cooked paella for lunch. In Spain, lunch is usually the 
biggest meal of the day. It's also very common for the people to take a midday nap right after a big meal. I am 
actually just waking up from my nap right now! 

On weekdays, I take classes at the local university. There, I met several native Spanish speakers. They have been 
very kind and patient with me. At first, I struggled to comprehend their Spanish, but now I understand most of our 
conversations. They have commented that my Spanish has improved a lot since we first met. Now, I am more confident to 
use the language in other places like stores and restaurants. '''


class Methods(TextChoices):
    extractive = "extractive_plus"
    py_sum = "py_sum"


class Summarize(Schema):
    text: str = initial_text
    method: Methods = "extractive_plus"


class SummarizeFile(Schema):
    method: Methods = "extractive_plus"

@api.post("/")
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def summarize_api_text(request, lang_text_schem: Summarize):
    validate_api_text(lang_text_schem.text)
    res = methods.get(lang_text_schem.method.name)(lang_text_schem.text)
    return {"result": res}


@api.post("/file")
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def summarize_api_file(request, method: SummarizeFile, file: UploadedFile = File(...)):
    validate_api_file(file)
    res = methods.get(method.method.name)(FileManager.file_read(file))
    return {"result": res}
