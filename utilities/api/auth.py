from ninja.security import APIKeyHeader

from utilities.api.compare_tokens import CompareTokens


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        return CompareTokens(input_token=key)()
