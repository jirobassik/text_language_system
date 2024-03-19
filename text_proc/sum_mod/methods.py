from text_proc.sum_mod.extractive_plus_summarizer import ExtractivePlusSummarize
from text_proc.sum_mod.py_summarizer import PySummarizer

methods = {
    'extractive': ExtractivePlusSummarize(),
    'py_sum': PySummarizer()
}
