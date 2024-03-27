from django.conf import settings

# Api common description
common_description = f"""<br><b>Limitations</b><br>Text: from {settings.API_VALID_MIN_FORM_LENGTH_TEXT} to 
{settings.API_VALID_MAX_FORM_LENGTH_TEXT} characters<br>File: from {settings.API_VALID_MIN_FILE_LENGTH_TEXT} 
to {settings.API_VALID_MAX_FILE_LENGTH_TEXT} characters. Extensions: {", ".join(settings.VALID_EXTENSIONS_FILE)}. 
The size is not more than 2 MB. <br> Requests: {settings.USER_MIN_THROTTLE} per minute and {settings.USER_DAY_THROTTLE} 
per day</p>"""

# Common response
common_response = {
    "responses": {
        400: {
            "description": "Error Response",
        },
        401: {"description": "Unauthorized"},
        404: {
            "description": "Not Found Response",
        },
        405: {
            "description": "Method Not Allowed",
        },
        422: {
            "description": "Unprocessable Content",
        },
    },
}
