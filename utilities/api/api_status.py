from utilities.base_text_lang.base_status import BaseStatus


class ApiStatus(BaseStatus):
    def __init__(self, request):
        self.request = request

    def __call__(self, input_text, *args, **kwargs):
        task_id = self.gen_result(input_text, **kwargs)
        return task_id
