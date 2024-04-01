from ninja.security import APIKeyHeader
from utilities.api.compare_tokens import CompareTokens


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if user_token := CompareTokens(input_token=key)():
            if (
                request.user
                and request.user.is_authenticated
                and user_token.pk == request.user.pk
            ):
                return user_token
            else:
                request.user = user_token
                return user_token
