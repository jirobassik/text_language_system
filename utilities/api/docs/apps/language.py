from utilities.api.docs.common import common_description, common_response

# Api main
description = f"""<p>API for language detection. {common_description}"""

# Responses
responses = common_response

# summarize_api_text
lang_detect_api_text_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Language detect text from string",
}

# summarize_api_file
lang_detect_api_file_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Language detect text from file",
}
