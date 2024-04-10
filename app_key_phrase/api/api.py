from ninja import File, Form
from ninja import UploadedFile
from ninja.errors import ValidationError
from ninja_extra import NinjaExtraAPI
from app_key_phrase.api.schems import KeyPhraseSchem, KeyPhraseSchemFile
from utilities.api.auth import ApiKey
from utilities.api.docs.multiple_docs import MixedDocs
from utilities.api.setup_throttle import (
    User60MinRateThrottle,
    User100PerDayRateThrottle,
)
from utilities.converter import convert_to_serializable
from utilities.validators.api_file_validations import validate_api_file
from utilities.file_manager.file import ApiFIleManager
from text_proc.key_phrase_mod.errors import KeyPhraseExtractorError
from text_proc.key_phrase_mod.key_phrase_extractor import KeyPhraseExtractor
from ninja_extra.throttling import throttle
from utilities.api.error import send_error
from utilities.api.docs.apps.key_phrase import (
    description,
    key_phrase_extractor_api_file_kwargs,
    key_phrase_extractor_api_text_kwargs,
    key_phrases_error_message,
)
from langdetect.lang_detect_exception import LangDetectException

api = NinjaExtraAPI(
    docs_url="/docs/<engine>",
    docs=MixedDocs(),
    auth=ApiKey(),
    title="Key phrase extractor API",
    urls_namespace="key_phrase_api",
    description=description,
)


@api.exception_handler(ValidationError)
def validation_error(request, exc):
    return send_error(exc)


@api.exception_handler(LangDetectException)
@api.exception_handler(KeyPhraseExtractorError)
def key_phrase_error(request, exc):
    exc.errors = key_phrases_error_message
    return send_error(exc)


@api.post("/", **key_phrase_extractor_api_text_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def key_phrase_extractor_api_text(request, key_phrase_schem: KeyPhraseSchem):
    res = KeyPhraseExtractor()(key_phrase_schem.text, key_phrase_schem.num_key_phrase)
    return {"result": convert_to_serializable(res)}


@api.post("/file", **key_phrase_extractor_api_file_kwargs)
@throttle(User60MinRateThrottle, User100PerDayRateThrottle)
def key_phrase_extractor_api_file(
    request, key_phrase_file_schem: Form[KeyPhraseSchemFile], file: UploadedFile = File(...)
):
    validate_api_file(file)
    res = KeyPhraseExtractor()(
        ApiFIleManager().file_read(file), key_phrase_file_schem.num_key_phrase
    )
    return {"result": convert_to_serializable(res)}
