from typing import Optional

from django.http import HttpRequest
from ninja_extra.throttling import SimpleRateThrottle

from utilities.api.compare_tokens import CompareTokens


class ApiTokenUserRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """

    scope = "user"

    def get_cache_key(self, request: HttpRequest) -> Optional[str]:
        if key := request.headers.get("X-Api-Key"):
            if ident_token := CompareTokens(input_token=key)():
                ident = ident_token
            else:
                ident = self.get_ident(request)
        else:
            ident = self.get_ident(request)

        return self.cache_format % {"scope": self.scope, "ident": ident}
