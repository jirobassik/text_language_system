from text_proc.lang_mod.langid_method import langid_method
from text_proc.lang_mod.short_word_method import ShortWord
from text_proc.lang_mod.lang_detect import lang_detect

short_word_method = ShortWord()

methods = {
    "short": short_word_method,
    "langdetect": lang_detect,
    "langid": langid_method,
}
