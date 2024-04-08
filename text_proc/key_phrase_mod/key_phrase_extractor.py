from yake import KeywordExtractor
from langdetect import detect
from text_proc.key_phrase_mod.errors import KeyPhraseExtractorError


class KeyPhraseExtractor:

    def __call__(self, text, num_keywords, *args, **kwargs):
        return self.match_language(text, num_keywords)

    @staticmethod
    def match_language(text, num_keywords=20):
        match detect(text):
            case "en":
                return KeywordExtractor(lan="en", top=num_keywords).extract_keywords(text)
            case "ru":
                return KeywordExtractor(lan="ru", top=num_keywords).extract_keywords(text)
        raise KeyPhraseExtractorError("Не удалось обработать текст")
