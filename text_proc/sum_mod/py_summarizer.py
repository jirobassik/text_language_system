from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


class PySummarizer:
    __slots__ = ('auto_abstractor', 'abstractable_doc')

    def __init__(self):
        self.auto_abstractor = AutoAbstractor()
        self.abstractable_doc = self.setting_auto_abs()

    def setting_auto_abs(self):
        self.auto_abstractor.tokenizable_doc = SimpleTokenizer()
        self.auto_abstractor.delimiter_list = [".", "\n"]
        return TopNRankAbstractor()

    def summarize_text(self, text: str):
        result_dict = self.auto_abstractor.summarize(text, self.abstractable_doc)
        return ''.join([sentence.replace('\n', '') for sentence in result_dict["summarize_result"]])
