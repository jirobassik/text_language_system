from django.db import models
from django.core.validators import MinLengthValidator


class LanguagePoaModel(models.Model):
    language = models.CharField(max_length=30, unique=True, validators=(MinLengthValidator(3),))
    short_name_language = models.CharField(max_length=30, unique=True, validators=(MinLengthValidator(1),))
    poa_text = models.TextField(max_length=6000, validators=(MinLengthValidator(3000),))

    class Meta:
        ordering = ["language"]
        indexes = [models.Index(fields=["language"])]
        verbose_name_plural = "ПОЯ тексты"

    def __str__(self):
        return self.language
