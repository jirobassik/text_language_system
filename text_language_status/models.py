import uuid
from django.contrib.auth.models import User
from django.db import models
from history.models import HistoryModel


class TextLanguageManagerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_id = models.CharField(verbose_name="ID задачи", max_length=100, unique=False)
    status = models.CharField(verbose_name="Статус задачи", max_length=100, null=False, blank=False)
    text = models.CharField("Текст", max_length=400, null=False, blank=False)
    time_add = models.DateTimeField(
        "Время добавления задачи", auto_created=True, editable=False, auto_now_add=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель задачи")
    history_id = models.OneToOneField(
        HistoryModel, on_delete=models.CharField, verbose_name="ID истории", null=True
    )
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False)
    executed = models.BooleanField(verbose_name="Выполнено", default=False)

    class Meta:
        verbose_name_plural = "Статус обработки"
        ordering = ["-time_add"]
        indexes = [models.Index(fields=("task_id", "time_add"))]

    def __str__(self):
        return self.task_id
