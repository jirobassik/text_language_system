from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from api_key.models import ApiKeyModel
from utilities.redis_com.sub_commands.delete_limit import delete_limit


@db_periodic_task(crontab(minute="*/1"), priority=100)
def check_expired_key():
    rows_updated = ApiKeyModel.objects.filter(
        expired_at__lt=timezone.now(), is_expired=False, is_deleted=False
    )
    for row in rows_updated:
        delete_limit(row.user.pk)
    rows_updated.update(is_expired=True, is_deleted=True)
