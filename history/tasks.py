from datetime import datetime, timedelta

from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from history.models import HistoryModel


@db_periodic_task(crontab(minute="*/1"), priority=100)
def delete_old_history():
    HistoryModel.objects.filter(created_at__lte=datetime.now() - timedelta(hours=24)).update(
        is_deleted=True
    )
