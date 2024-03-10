from secrets import token_hex
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def generate_api_key(key_len=32):
    return token_hex(key_len)


class ApiKeyModel(models.Model):
    api_token = models.CharField('API ключ', default=generate_api_key, editable=False, unique=True)
    created_at = models.DateTimeField('Время добавления', auto_created=True, editable=False, auto_now_add=True)
    expired_at = models.DateTimeField('Время истечения', editable=True, auto_created=True,
                                      default=timezone.now() + timezone.timedelta(weeks=1))
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False)
    is_expired = models.BooleanField(verbose_name='Истек', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.api_token

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=("created_at", "expired_at", "is_deleted", "is_expired",))
        ]
