from huey.contrib.djhuey import db_task
from utilities.task.common_task_ex import create_history_update_status_delete_limit


@db_task(priority=90, expires=600)
def extraction_task(user, task_model_pk, choose_input_text, **kwargs):
    create_history_update_status_delete_limit(
        user, task_model_pk, choose_input_text, **kwargs
    )
