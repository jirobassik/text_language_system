from django.conf import settings

# Api common description
common_description = f"""<br><b>Limitations</b><br>Text: from {settings.API_VALID_MIN_FORM_LENGTH_TEXT} to 
{settings.API_VALID_MAX_FORM_LENGTH_TEXT} characters<br>File: from {settings.API_VALID_MIN_FILE_LENGTH_TEXT} 
to {settings.API_VALID_MAX_FILE_LENGTH_TEXT} characters. Extensions: {", ".join(settings.VALID_EXTENSIONS_FILE)}. 
The size is not more than 2 MB. <br> Requests: {settings.USER_MIN_THROTTLE} per minute and {settings.USER_DAY_THROTTLE} 
per day</p>"""

common_file_error_message = [
    {
        "type": "failed_read_file",
        "msg": "Try input other file",
    }
]


# Common error
common_error = {
    "content": {
        "application/json": {
            "schema": {
                "type": "object",
                "properties": {
                    "detail": {
                        "type": ["string", "list"],
                        "description": "Error message",
                    },
                },
            }
        },
    },
}

# Common ok
common_ok = {
    "content": {
        "application/json": {
            "schema": {
                "type": "object",
                "properties": {
                    "result": {
                        "type": "string",
                        "description": "Result text",
                    },
                },
            }
        },
    },
}

error_response = {
    400: {"description": "Error Response", **common_error},
    401: {"description": "Unauthorized", **common_error},
    404: {"description": "Not Found Response", **common_error},
    405: {"description": "Method Not Allowed", **common_error},
    422: {"description": "Unprocessable Content", **common_error},
}

# Common response
common_response = {
    "responses": {
        200: {"description": "OK", **common_ok},
        **error_response
    },
}


