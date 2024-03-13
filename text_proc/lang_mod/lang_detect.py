from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


def lang_detect(text):
    try:
        return detect(text)
    except LangDetectException:
        return 'Не удалось определить язык'
