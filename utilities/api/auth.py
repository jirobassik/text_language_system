from ninja.security import APIKeyHeader

from api_key.models import ApiKeyModel


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            return ApiKeyModel.objects.filter(api_token=key, is_expired=False, is_deleted=False)
        except ApiKeyModel.DoesNotExist:
            pass
