import requests
from django.conf import settings


class Request:
    def __init__(self):
        self.__server_name = settings.NGROK_HTTP_URL

    # def get_request(self, data):
    #     return requests.get(
    #         f"{self.server_name + self.model_name}/",
    #         data=data,
    #         headers={"Content-Type": "application/json"},
    #         verify=ssl.CERT_NONE,
    #     )  # Попробовать {'Connection':'Keep-Alive'}

    def post_request_data(self, body_data):
        return requests.post(
            self.server_name,
            json={"text": body_data},
        )

    @property
    def server_name(self):
        return self.__server_name
