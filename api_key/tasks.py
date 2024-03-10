from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from api_key.models import ApiKeyModel


@db_periodic_task(crontab(minute='*/1'))
def add_response_api_converter():
    ApiKeyModel.objects.filter(expired_at__lt=timezone.now(), is_expired=False, is_deleted=False).update(
        is_expired=True, is_deleted=True)
