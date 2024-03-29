from secrets import token_hex
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


def generate_api_key(key_len=32):
    return token_hex(key_len)


def default_expired_at():
    return timezone.now() + timezone.timedelta(weeks=1)


class ApiKeyModel(models.Model):
    api_token = models.CharField("API ключ", editable=False, unique=True)
    created_at = models.DateTimeField(
        "Время добавления", auto_created=True, editable=False, auto_now_add=True
    )
    expired_at = models.DateTimeField(
        "Время истечения", editable=True, auto_created=True, default=default_expired_at
    )
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False)
    is_expired = models.BooleanField(verbose_name="Истек", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return "API токен хэширован. Можно только удалить и создать новый"

    def get_absolute_key_delete_url(self):
        return reverse('api-key-delete-view', args=[self.id])

    class Meta:
        verbose_name_plural = "API токены"
        ordering = ["created_at"]
        indexes = [
            models.Index(
                fields=(
                    "created_at",
                    "expired_at",
                    "is_deleted",
                    "is_expired",
                )
            )
        ]
