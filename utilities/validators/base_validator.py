from django.core.validators import BaseValidator
from ninja.errors import ValidationError


class ApiBaseValidator(BaseValidator):
    def __call__(self, value):
        cleaned = self.clean(value)
        limit_value = (
            self.limit_value() if callable(self.limit_value) else self.limit_value
        )
        if self.compare(cleaned, limit_value):
            raise ValidationError(self.message)
