from utilities.api.docs.common import common_description, common_response

# Api main
description = f"""<p>API for key phrase extraction. {common_description}"""

# Field descriptions
num_key_phrases_description = "Maximum number of key phrases from text"

# Responses
responses = common_response

# Errors messages
key_phrases_error_message = [
    {
        "type": "not_extract_key_phrase_error",
        "msg": "Try input other sentence",
    }
]

# key_phrase_extractor_api_text
key_phrase_extractor_api_text_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Key phrase extraction from string",
}

# key_phrase_extractor_api_file
key_phrase_extractor_api_file_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Key phrase extraction from file",
}
