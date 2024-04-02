from history.models import HistoryModel
from text_language_status.models import TextLanguageManagerModel


def create_history_update_status(user, task_model_pk, choose_input_text, res):
    his_obj = HistoryModel.objects.create(user=user, input_text=choose_input_text, result_text=res)
    TextLanguageManagerModel.objects.filter(id=task_model_pk, user=user).update(
        history_id=his_obj.id, executed=True
    )
