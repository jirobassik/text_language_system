import time
from collections import Counter
from string import ascii_letters
from itertools import chain
from utilities.textnormalizer import TextNormalizer


class Alphabets:
    __slots__ = ('english_letters', 'finnish_letters', 'german_letters', 'russian_letters')

    def __init__(self):
        self.english_letters = ascii_letters
        self.german_letters = ascii_letters + 'ÄÖÜẞäöüß'
        self.finnish_letters = ascii_letters + 'ÄÖäö'
        self.russian_letters = self.__russian_letters_def()

    @staticmethod
    def __russian_letters_def() -> str:
        start_unicode_point_rus = ord('а')
        lower_rus_letters = ''.join(
            chain([chr(unicode_alph) for unicode_alph in range(start_unicode_point_rus, start_unicode_point_rus + 6)],
                  [chr(start_unicode_point_rus + 33)],
                  [chr(unicode_alph) for unicode_alph in
                   range(start_unicode_point_rus + 6, start_unicode_point_rus + 32)]))
        upper_rus_letters = lower_rus_letters.upper()
        return lower_rus_letters + upper_rus_letters


class AlphabetMethod(Alphabets):

    def __init__(self):
        super().__init__()
        self.text_normalizer = TextNormalizer(remove_punctation=True, join_text=True)

    def __count_letters(self, text):
        text_counter = Counter(self.text_normalizer(text))
        return text_counter, text_counter.total()

    def alphabet_method_many_files(self, *args):
        dict_percent_files = {}
        start_time = time.time()
        for filename in args:
            engl_percent, rus_percent = self.__letter_percent(filename)
            dict_percent_files[filename] = 'english' if engl_percent > rus_percent else 'russian'
        res_time = time.time() - start_time
        return dict_percent_files, res_time

    def alphabet_method_one_file(self, text: str):
        engl_percent, rus_percent = self.__letter_percent(text)
        percent_dict = {'english_percent': engl_percent, 'russian_percent': rus_percent}
        return ('english', percent_dict['english_percent']) if percent_dict['english_percent'] > percent_dict[
            'russian_percent'] else ('russian', percent_dict['russian_percent'])

    def __letter_percent(self, text: str):
        alph_counter, all_alphs = self.__count_letters(text)
        engl_percent = self.__calculate_alph_percents(self.english_letters, alph_counter, all_alphs)
        rus_percent = self.__calculate_alph_percents(self.russian_letters, alph_counter, all_alphs)
        ger_percent = self.__calculate_alph_percents(self.german_letters, alph_counter, all_alphs)
        finnish_percent = self.__calculate_alph_percents(self.finnish_letters, alph_counter, all_alphs)
        print('german pecent', ger_percent)
        print('finnish pecent', finnish_percent)
        return engl_percent, rus_percent

    @staticmethod
    def __calculate_alph_percents(letters: str, alph_counter: Counter, all_alphs: int):
        return sum(((alph_counter.get(alph, 0) / all_alphs) * 100 for alph in letters))


german_text = '''Minun nimeni on Ella ja olen kahdeksantoista vuotias. Käyn lukion toista vuotta Turussa, mutta olen kotoisin Oulusta.

Maanantaista torstaihin herään viisitoista yli seitsemän. Perjantaisin herään kahdeksalta, koska oppituntini alkavat myöhemmin. Herättyäni syön aamupalaa, puen päälleni ja menen kouluun.

Koulupäiväni päättyy kello kolmelta ja iltapäivällä syön kotona. Rakastan ruoanlaittoa, mutta välillä olen väsynyt, enkä jaksa tehdä ruokaa. Silloin menen ulos syömään.

Ennen päivällistä minulla on tanssiharjoitukset, jotka päättyvät puoli viideltä. Käyn harjoituksissa kolme kertaa viikossa. Olen harrastanut tanssia neljä vuotta.

Päivällisen jälkeen teen läksyni ja jos minulla on aikaa näen ystäviäni. Viikonloppuisin menemme elokuviin tai rannalle. Aina minulla ei ole aikaa, koska viikonloppuisin minulla on töitä. Työskentelen kotini lähellä olevassa ruokakaupassa.

Iltaisin katson televisiota tai luen. Rakastan kirjoja! Suosikki kirjojani on mysteeri kirjat. Haluan olla isona kirjailija.'''

# a = AlphabetMethod().alphabet_method_one_file(german_text)
# print(a)
