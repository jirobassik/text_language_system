from yake import KeywordExtractor
from langdetect import detect
from text_proc.key_phrase_mod.errors import KeyPhraseExtractorError
from collections import namedtuple


class NamedTupleKeywordExtractor(KeywordExtractor):
    key_phrase = namedtuple("KeyPhrase", ["key_phrase", "score"])

    def extract_keywords(self, text):
        keywords = super().extract_keywords(text)
        return [self.key_phrase(keyword, score) for keyword, score in keywords]


class KeyPhraseExtractor:

    def __call__(self, text, num_keywords, *args, **kwargs):
        return self.match_language(text, num_keywords)

    @staticmethod
    def match_language(text, num_keywords=20):
        match detect(text):
            case "en":
                return NamedTupleKeywordExtractor(
                    lan="en", top=num_keywords
                ).extract_keywords(text)
            case "ru":
                return NamedTupleKeywordExtractor(
                    lan="ru", top=num_keywords
                ).extract_keywords(text)
        raise KeyPhraseExtractorError("Не удалось обработать текст")
