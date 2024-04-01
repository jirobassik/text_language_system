from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from api_key.models import ApiKeyModel


class CompareTokens:
    def __init__(self, input_token: str):
        self.input_token = input_token

    def __call__(self, *args, **kwargs):
        try:
            return self.__check_token()
        except (ApiKeyModel.DoesNotExist, ValidationError, IndexError, AttributeError):
            pass

    def __get_api_key_obj(self):
        uuid_api_key = self.input_token.split(".")[1]
        return ApiKeyModel.objects.get(id=uuid_api_key, is_deleted=False, is_expired=False)

    def __check_token(self):
        api_key_obj = self.__get_api_key_obj()
        return (
            api_key_obj.user if check_password(self.input_token, api_key_obj.api_token) else None
        )
