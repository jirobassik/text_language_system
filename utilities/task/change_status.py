from types import MappingProxyType
from text_language_status.models import TextLanguageManagerModel
from utilities.redis_com.sub_commands.limit_long_operation import delete_long_operation


def update_status(task_id: str, status: str, task_pk, user, original_status):
    filter_task_id = TextLanguageManagerModel.objects.filter(
        id=task_pk, user=user, is_deleted=False
    )
    filter_task_id.update(status=status)
    update_limit_status(original_status, user, task_pk)


def update_limit_status(status, user, task_id):
    if status in {"error", "locked", "revoked", "interrupted", "expired"}:
        delete_long_operation(user, task_id)


status_choice = MappingProxyType(
    {
        "executing": "Выполняется",
        "complete": "Завершен",
        "error": "Ошибка",
        "locked": "Ошибка",
        "revoked": "Отменена",
        "interrupted": "Ошибка",
        "expired": "Срок истек",
        "retrying": "Повторное выполнение",
        "scheduled": "Добавлено в расписание",
    }
)
