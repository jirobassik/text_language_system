from utilities.api.docs.common import error_response

# Api main
description = f"""<p>API for get result from long tasks."""


# Responses
responses = {
    "responses": {**error_response},
}

# history_detail
history_api_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Get one history object",
}
