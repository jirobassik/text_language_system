from ninja.security import APIKeyHeader

from utilities.api.compare_tokens import CompareTokens


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if request.user and request.user.is_authenticated:
            if (pk_user_token := CompareTokens(input_token=key)()) and pk_user_token == request.user.pk:
                return pk_user_token
        else:
            return CompareTokens(input_token=key)()
