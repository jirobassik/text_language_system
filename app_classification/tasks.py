from huey.contrib.djhuey import db_task
from utilities.task.common_task_ex import create_history_update_status_delete_limit
from text_proc.clas_mod.neuro_classification import NeuroTextClassifier

@db_task(priority=90, expires=600)
def classify_long_task(user, task_model_pk, choose_input_text):
    res = ", ".join(NeuroTextClassifier()(choose_input_text))
    create_history_update_status_delete_limit(user, task_model_pk, choose_input_text, res)
