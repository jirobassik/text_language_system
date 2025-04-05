from huey.contrib.djhuey import revoke_by_id

from apps.text_language_status.models import TextLanguageManagerModel
from django.shortcuts import get_object_or_404


def revoke_task(task_id, user):
    status_obj = get_object_or_404(
        TextLanguageManagerModel, user=user, id=task_id, is_deleted=False
    )
    status_obj.status = "В очереди на отмену"
    status_obj.save()
    revoke_by_id(status_obj.task_id)
