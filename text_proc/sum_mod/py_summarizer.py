from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


class PySummarizer:
    __slots__ = ('auto_abstractor',)

    def __init__(self):
        self.auto_abstractor = AutoAbstractor()
        self.setting_auto_abs()

    def __call__(self, text: str, num_sentence: int):
        top_n_rank = TopNRankAbstractor()
        top_n_rank.top_n = num_sentence
        result_dict = self.auto_abstractor.summarize(text, top_n_rank)
        return ''.join([sentence.replace('\n', '') for sentence in result_dict["summarize_result"]])

    def setting_auto_abs(self):
        self.auto_abstractor.tokenizable_doc = SimpleTokenizer()
        self.auto_abstractor.delimiter_list = [".", "\n"]
