from langdetect import detect
from lang_mod.langid_method import langid_method
from lang_mod.short_word_method import ShortWord

short_word_method = ShortWord()

methods = {
    'short': short_word_method,
    'langdetect': detect,
    'langid': langid_method,
}
