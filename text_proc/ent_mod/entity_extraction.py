from collections import defaultdict
from langdetect import detect
import spacy
from text_proc.ent_mod.errors import EntityExtractionError


class EntityExtraction:
    nlp_eng = spacy.load("en_core_web_sm")
    nlp_ru = spacy.load("ru_core_news_sm")

    def __call__(self, text, *args, **kwargs):
        return self.match_language(text)

    def match_language(self, text):
        match detect(text):
            case "en":
                return self.group_entities(self.nlp_eng(text))
            case "ru":
                return self.group_entities(self.nlp_ru(text))
        raise EntityExtractionError("Не удалось обработать текст")

    @staticmethod
    def group_entities(doc):
        entity_dict = defaultdict(set)
        for entity in doc.ents:
            entity_dict[entity.label_].add(entity.text)
        return dict(entity_dict)
