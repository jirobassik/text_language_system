from typing import Optional

from django.http import HttpRequest
from ninja_extra.throttling import SimpleRateThrottle

from api_key.models import ApiKeyModel


class ApiTokenUserRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """

    scope = "user"

    def get_cache_key(self, request: HttpRequest) -> Optional[str]:
        if request.user and request.user.is_authenticated:
            ident = request.user.pk
        elif key := request.headers.get('X-Api-Key'):
            try:
                ident = ApiKeyModel.objects.get(api_token=key).user.pk
            except ApiKeyModel.DoesNotExist:
                ident = self.get_ident(request)
        else:
            ident = self.get_ident(request)

        return self.cache_format % {"scope": self.scope, "ident": ident}
