from types import MappingProxyType
from text_language_status.models import TextLanguageManagerModel


def update_status(task_id: str, status: str, task_pk, user):
    filter_task_id = TextLanguageManagerModel.objects.filter(
        id=task_pk, user=user, is_deleted=False
    )
    filter_task_id.update(task_id=task_id, status=status)


status_choice = MappingProxyType(
    {
        "executing": "Выполняется",
        "complete": "Завершен",
        "error": "Ошибка",
        "locked": "Ошибка",
        "revoked": "Ошибка",
        "interrupted": "Ошибка",
        "expired": "Срок истек",
        "retrying": "Повторное выполнение",
        "scheduled": "Добавлено в расписание",
    }
)
