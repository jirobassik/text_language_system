from math import log
from operator import getitem
from nltk import sent_tokenize
from text_proc.textnormalizer import TextNormalizer


class StandartTextSummarize:
    __slots__ = ('text_normalizer',)

    def __init__(self):
        self.text_normalizer = TextNormalizer(remove_punctation=True, remove_number=True)

    def summarize_text(self, text: str):
        text_without_n = text
        list_sentence_tokenize = sent_tokenize(text_without_n)
        scores = self.calculate_weight_sentences(text_without_n, list_sentence_tokenize)
        sentence_score = zip(list_sentence_tokenize, scores)
        sorted_sentence_score = dict(sorted(sentence_score, key=lambda item: getitem(item, 1), reverse=True))
        return ' '.join(list(sorted_sentence_score.keys())[:10])

    def calculate_weight_sentences(self, text: str, sent_tokenize_: list):
        list_words, list_sentences = self.text_normalizer(text), list(map(self.text_normalizer, sent_tokenize_))
        scores = []
        for sentences in list_sentences:
            score = 0
            for word in sentences:
                score += self.__term_frequency(sentences, word) * \
                         self.__inverse_document_frequency(word, list_words, list_sentences)
            scores.append(score)
        return scores

    @staticmethod
    def __term_frequency(sentence: list, word: str):
        try:
            term_freq = sentence.count(word) / len(sentence)
        except ZeroDivisionError:
            term_freq = 0.000001
        return term_freq

    def __inverse_document_frequency(self, word: str, list_words: list, list_sentences: list):
        return 0.5 * (1 + self.__term_frequency(list_words, word) / self.__max_frequency(list_sentences, word)) * \
            log(len(list_sentences) / 1)  # Что делать с еденицией

    def __max_frequency(self, list_sentences: list, word: str):
        term_frequency = 0
        for sentence in list_sentences:
            if term_frequency < (new_term_freq := self.__term_frequency(sentence, word)):
                term_frequency = new_term_freq
        return term_frequency
