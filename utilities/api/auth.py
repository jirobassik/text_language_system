from ninja.security import APIKeyHeader

from api_key.models import ApiKeyModel


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            return ApiKeyModel.objects.get(api_token=key)
        except ApiKeyModel.DoesNotExist:
            pass
