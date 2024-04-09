from utilities.api.docs.common import common_description, error_response

# Api main
description = f"""<p>API for text classification. {common_description}"""

# Responses
error_responses = error_response

# classify_api_text
classify_api_text_kwargs = {
    "openapi_extra": {**error_responses},
    "summary": "Classify text from string",
}

# classify_api_file
classify_api_file_kwargs = {
    "openapi_extra": {**error_responses},
    "summary": "Classify text from file",
}
