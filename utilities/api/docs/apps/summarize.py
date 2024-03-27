from utilities.api.docs.common import common_description, common_response

# Api main
description = f"""<p>API for text summarize. {common_description}"""

# Field descriptions
num_sentence_description = "Maximum number of sentences in abstracted text"

# Responses
responses = common_response

# summarize_api_text
summarize_api_text_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Summarize text from string",
}

# summarize_api_file
summarize_api_file_kwargs = {
    "openapi_extra": {**responses},
    "summary": "Summarize text from file",
}
