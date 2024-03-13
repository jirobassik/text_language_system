import re
from string import punctuation
from collections import namedtuple

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from toolz import pipe


class TextProc:
    __slots__ = ('text',)

    def __init__(self, text):
        self.text = text
        self.__text_proc()

    def __remove_urls(self):
        pattern = r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
        self.text = re.sub(pattern, "", self.text)
        return self

    def __remove_html(self):
        pattern = r"<[^>]+>"
        self.text = re.sub(pattern, "", self.text)
        return self

    def __text_proc(self):
        return self.__remove_html().__remove_urls()

    def get_text(self):
        return self.text


class TextNormalizer:
    __slots__ = ('text_pre_proc', 'proc_text', 'world_len', 'priority_name_using', 'methods')

    def __init__(self, remove_punctation=True, lowercase=False, lemmatize=False, remove_number=False,
                 remove_world_ge=False, join_text=False, text_pre_proc=True, world_len=3):
        self.text_pre_proc = text_pre_proc
        self.proc_text = TextProc
        self.world_len = self.define_world_len(world_len)
        self.priority_name_using = namedtuple('priority_name', 'priority name using')
        self.methods = {self.priority_name_using(1, 'remove_punctation', remove_punctation): self.remove_punctation,
                        self.priority_name_using(1, 'lowercase', lowercase): self.lowercase,
                        self.priority_name_using(1, 'lemmatize', lemmatize): self.lemmatize,
                        self.priority_name_using(1, 'remove_number', remove_number): self.remove_number,
                        self.priority_name_using(2, 'remove_world_ge', remove_world_ge): self.remove_world_ge,
                        self.priority_name_using(3, 'join_text', join_text): self.join_text}

    def __call__(self, text, *args, **kwargs):
        filter_dict = self.define_proc_methods()
        tokenize_text = word_tokenize(self.define_text(text))
        return pipe(tokenize_text, *filter_dict.values())

    def define_proc_methods(self):
        # def_methods = dict(sorted(filter(self.filter_dict_meth, self.methods.items()),
        #                           key=lambda pair: pair[0].priority))
        if not (def_methods := dict(sorted(filter(self.filter_dict_meth, self.methods.items()),
                                           key=lambda pair: pair[0].priority))):
            raise ValueError('No one methods been defined')
        return def_methods

    @staticmethod
    def define_world_len(world_len):
        if world_len <= 0:
            raise ValueError('World len must be greater 0')
        return world_len

    def define_text(self, text):
        return self.proc_text(text).get_text() if self.text_pre_proc else text

    @staticmethod
    def filter_dict_meth(pair):
        return True if pair[0].using else False

    @staticmethod
    def remove_punctation(token_text):
        table = str.maketrans('', '', punctuation)
        return [word.translate(table) for word in token_text if word not in punctuation]

    @staticmethod
    def lowercase(token_text):
        return [word.lower() for word in token_text]

    @staticmethod
    def lemmatize(token_text):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in token_text]

    @staticmethod
    def remove_number(token_text):
        return [word for word in token_text if not word.isnumeric()]

    def remove_world_ge(self, token_text: list[str]):
        return [word for word in token_text if len(word) <= self.world_len or not word.isalpha()]

    @staticmethod
    def join_text(token_text):
        return ''.join(token_text)
