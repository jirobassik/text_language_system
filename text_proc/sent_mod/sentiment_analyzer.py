from collections import namedtuple

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
from langdetect import detect

from text_proc.sent_mod.errors import SentimentAnalyzerError
from text_proc.sent_mod.train_data.rus import sentences_rus

cl = NaiveBayesClassifier(sentences_rus)


class SentimentAnalyzer:
    RETURN_TYPE = namedtuple("Sentiment", ["classification", "p_pos", "p_neg"])

    def __call__(self, text, *args, **kwargs):
        return self.match_language(text)

    def match_language(self, text):
        match detect(text):
            case "en":
                return TextBlob(text, analyzer=NaiveBayesAnalyzer()).sentiment
            case "ru":
                prob_dist = cl.prob_classify(text)
                return self.RETURN_TYPE(
                    classification=prob_dist.max(),
                    p_pos=round(prob_dist.prob("pos"), 2),
                    p_neg=round(prob_dist.prob("neg"), 2),
                )
        raise SentimentAnalyzerError("Не удалось обработать текст")
