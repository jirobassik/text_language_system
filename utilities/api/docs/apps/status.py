from utilities.api.docs.common import error_response

# Api main
description = f"""<p>API for get status long task with result from history."""


# Responses
responses = {
    "responses": {**error_response},
}

# status_detail
status_api_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Get status with history",
}

# revoke_task
revoke_status_api_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Revoke task from status",
}
