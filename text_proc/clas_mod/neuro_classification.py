import json

from utilities.server_request.server import Request
from utilities.server_request.error import SendError

class NeuroTextClassifier:
    request_text_classification = Request()

    def __call__(self, text, *args, **kwargs):
        return self.send_classification_request(text)

    def send_classification_request(self, text):
        response_classification = self.request_text_classification.post_request_data(text)
        if response_classification.status_code == 200:
            data = response_classification.json()
            return json.loads(data["result"])
        raise SendError
