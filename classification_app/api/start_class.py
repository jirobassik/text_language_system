from classification_app.tasks import classify_long_task
from utilities.api.api_status import ApiStatus


class ClassifyApiStart(ApiStatus):
    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        return classify_long_task(user, task_model_pk, choose_input_text, **kwargs)
