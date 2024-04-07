from ninja import File
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from app_sentiment.api.schems import SentimentSchem, SentimentOut
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from text_proc.sent_mod.errors import SentimentAnalyzerError
from text_proc.sent_mod.sentiment_analyzer import SentimentAnalyzer
from ninja_extra.throttling import throttle
from utilities.api.error import send_error
from utilities.api.docs.apps.sentiment import sentiment_error_message
from utilities.api.docs.apps.sentiment import (
    description,
    sentiment_analyzer_file_kwargs,
    sentiment_analyzer_text_kwargs,
)
from langdetect.lang_detect_exception import LangDetectException

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Sentiment analyzer API",
    urls_namespace="sent_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_error(request, exc):
    return send_error(exc)


@api.exception_handler(LangDetectException)
@api.exception_handler(SentimentAnalyzerError)
def sentiment_error(request, exc):
    exc.errors = sentiment_error_message
    return send_error(exc)


@api.post("/", response=SentimentOut, **sentiment_analyzer_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def sentiment_analyzer_api_text(request, lang_text_schem: SentimentSchem):
    res = SentimentAnalyzer()(lang_text_schem.text)
    return {"result": res.classification, "p_pos": res.p_pos, "p_neg": res.p_neg}


@api.post("/file", response=SentimentOut, **sentiment_analyzer_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def sentiment_analyzer_api_file(request, file: UploadedFile = File(...)):
    validate_api_file(file)
    res = SentimentAnalyzer()(ApiFIleManager().file_read(file))
    return {"result": res.classification, "p_pos": res.p_pos, "p_neg": res.p_neg}
