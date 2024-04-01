from text_language_status.models import TextLanguageManagerModel


class BaseStatus:
    def gen_result(self, choose_input_text, **kwargs):
        user, task_model = self.create_manager_field(text=f"{choose_input_text[:30]}...")
        self.add_queue(user, task_model, choose_input_text, **kwargs)

    def create_manager_field(self, task_id="Не задан", text="Обрабатывается", status="В очереди"):
        user = self.request.user
        task_model = TextLanguageManagerModel.objects.create(
            task_id=task_id, text=text, status=status, user=user
        )
        return user, task_model

    def setup_long_task(self, user, task_model_pk, choose_input_text, **kwargs):
        raise NotImplementedError

    def add_queue(self, user, task_model, choose_input_text, **kwargs):
        task_model_pk = task_model.pk
        self.setup_long_task(user, task_model_pk, choose_input_text, **kwargs)
