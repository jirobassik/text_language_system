import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class HistoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    input_text = models.TextField("Введенный текст", max_length=10000)
    result_text = models.TextField("Результата обработки", max_length=10000)
    created_at = models.DateTimeField(
        "Время добавления", auto_created=True, editable=False, auto_now_add=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    is_deleted = models.BooleanField("Удален", default=False)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at", "is_deleted"])]
        verbose_name_plural = "История"

    def get_absolute_url(self):
        return reverse("history-detail-view", args=[self.id])
