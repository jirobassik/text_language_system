from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from langdetect import detect

from text_proc.sent_mod.errors import SentimentAnalyzerError


class SentimentAnalyzer:
    def __call__(self, text, *args, **kwargs):
        return self.match_language(text)

    @staticmethod
    def match_language(text):
        match detect(text):
            case "en":
                return TextBlob(text, analyzer=NaiveBayesAnalyzer()).sentiment.classification
            case "ru":
                return "Russian"
        raise SentimentAnalyzerError("Не удалось обработать текст")
