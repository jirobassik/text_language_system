from django.urls import reverse_lazy
from django.views.generic import FormView
from django.conf import settings
from api_key.forms import ApiKeyForm
from api_key.models import ApiKeyModel, generate_api_key
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from utilities.redis_com import check_limit, api_update_limit_check


class ApiKeyView(LoginRequiredMixin, FormView):
    form_class = ApiKeyForm
    template_name = 'api_key/api_key_form.html'
    success_url = reverse_lazy('api-key-view')

    def get_context_data(self, **kwargs):
        context = super(ApiKeyView, self).get_context_data(**kwargs)
        context['key'] = self.get_api_key()
        context['max_throttle'] = settings.USER_DAY_THROTTLE
        context['block_update_but'] = check_limit(self.request.user.pk)
        return context

    def form_valid(self, form):
        if self.get_api_key():
            self.update_api_key()
        else:
            form.instance.user = self.request.user
            form.save()
        return super().form_valid(form)

    def update_api_key(self):
        ApiKeyModel.objects.filter(user=self.request.user, is_deleted=False, is_expired=False).update(
            api_token=generate_api_key())
        api_update_limit_check(self.request.user.pk)

    def get_api_key(self):
        try:
            return ApiKeyModel.objects.get(user=self.request.user, is_deleted=False, is_expired=False)
        except ObjectDoesNotExist:
            return False
