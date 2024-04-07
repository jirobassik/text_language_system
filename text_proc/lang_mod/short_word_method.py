import time
from functools import cache

from text_proc.textnormalizer import TextNormalizer
from collections import Counter
from operator import ge, getitem
from decimal import Decimal
from app_language.models import LanguagePoaModel


class ShortWord:
    __slots__ = ("text_normalizer",)

    def __init__(self):
        self.text_normalizer = TextNormalizer(
            remove_punctation=True, remove_world_ge=True, remove_number=True
        )

    def __call__(self, text, *args, **kwargs):
        input_preprocess_text = self.text_normalizer(text.lower())
        start = time.time()
        res_dict_short_meth = self.__file_probability(input_preprocess_text)
        end = time.time() - start
        print("end time", end)
        return max(res_dict_short_meth, key=res_dict_short_meth.get)

    @cache
    def __languages_probability(self):
        return {
            language_poa.short_name_language: self.__create_poa(language_poa.poa_text)
            for language_poa in LanguagePoaModel.objects.all()
        }

    def __create_poa(self, text: str):
        preprocess_pdf_text = self.text_normalizer(text.lower())
        counter_words = Counter(preprocess_pdf_text)
        counter_num_short_words = self.__counter_number_short_words(counter_words)
        number_all_worlds = sum(counter_num_short_words.values())
        dict_probability_worlds = self.__calculate_probability_each_world(
            counter_num_short_words, number_all_worlds
        )
        return dict_probability_worlds

    def __file_probability(self, worlds: list):
        return {
            language: self.__calculate_probability(worlds, probability)
            for language, probability in self.__languages_probability().items()
        }

    @staticmethod
    def __counter_number_short_words(counter: dict):
        return dict(filter(lambda short_word: ge(getitem(short_word, 1), 3), counter.items()))

    @staticmethod
    def __calculate_probability_each_world(counter: dict, all_words_counter: int):
        return {
            short_word: num_short_word / all_words_counter
            for short_word, num_short_word in counter.items()
        }

    @staticmethod
    def __calculate_probability(text_words: list, counter_probability: dict):
        probability = Decimal(1.0)
        for word in text_words:
            if word.lower() in counter_probability.keys():
                probability *= Decimal(counter_probability.get(word, 0.01))
            else:
                probability *= Decimal(0.01)
        return probability
