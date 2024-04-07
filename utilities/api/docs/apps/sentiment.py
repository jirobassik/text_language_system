from utilities.api.docs.common import common_description, error_response

# Api main
description = f"""<p>API for sentiment analyze. {common_description}"""

# Errors messages
sentiment_error_message = [
    {
        "type": "not_define_sentiment",
        "msg": "Try input other sentence",
    }
]

# sentiment_analyzer_api_text
sentiment_analyzer_text_kwargs = {
    "openapi_extra": {**error_response},
    "summary": "Sentiment analyze text from string",
}

# sentiment_analyzer_api_file
sentiment_analyzer_file_kwargs = {
    "openapi_extra": {**error_response},
    "summary": "Sentiment analyze text from file",
}
