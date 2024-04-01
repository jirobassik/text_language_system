from datetime import datetime, timedelta
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from huey.contrib.djhuey import signal
from text_language_status.models import TextLanguageManagerModel
from utilities.task.change_status import update_status, status_choice


@db_periodic_task(crontab(minute="*/1"), priority=100)
def delete_old_status():
    TextLanguageManagerModel.objects.filter(
        time_add__lte=datetime.now() - timedelta(hours=1)
    ).update(is_deleted=True)


@signal()
def signal_listener(signal, task, exc=None):
    if task.name == "classify_long_task":
        task_user, task_pk = task.args[0], task.args[1]
        update_status(task.id, status_choice.get(signal, "Нет данных"), task_pk, task_user)
