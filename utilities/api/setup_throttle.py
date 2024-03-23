from django.conf import settings

from utilities.api.custom_throttle import ApiTokenUserRateThrottle


class User60MinRateThrottle(ApiTokenUserRateThrottle):
    rate = f"{settings.USER_MIN_THROTTLE}/min"
    scope = "minutes"


class User100PerDayRateThrottle(ApiTokenUserRateThrottle):
    rate = f"{settings.USER_DAY_THROTTLE}/day"
    scope = "days"
