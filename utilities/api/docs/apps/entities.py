from utilities.api.docs.common import common_description, common_response

# Api main
description = f"""<p>API for extraction entities. {common_description}"""

# Responses
responses = common_response

# Errors messages
ent_extr_error_message = [
    {
        "type": "not_extract_entities",
        "msg": "Try input other sentence",
    }
]

# entities_extraction_api_text
entities_extraction_api_text_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Extraction entities text from string",
}

# entities_extraction_api_file
entities_extraction_api_file_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Extraction entities text from file",
}
