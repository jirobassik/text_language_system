from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView
from django.conf import settings
from api_key.forms import ApiKeyForm
from api_key.models import ApiKeyModel
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from utilities.redis_com.sub_commands.delete_limit import check_limit, api_delete_limit_check
from utilities.api.gen_api_key import generate_api_key


class ApiKeyView(LoginRequiredMixin, FormView):
    form_class = ApiKeyForm
    template_name = "api_key/api_key_form.html"
    success_url = reverse_lazy("api-key-view")

    def get_context_data(self, **kwargs):
        context = super(ApiKeyView, self).get_context_data(**kwargs)
        context["object_api"] = self.get_object_api()
        context["max_throttle"] = settings.USER_DAY_THROTTLE
        return context

    def form_valid(self, form):
        if object_api := self.get_object_api():
            return redirect(object_api.get_absolute_key_delete_url())
        else:
            api_key = self.create_api_key(form)
            context = self.get_context_data()
            context["api_key"] = api_key
            return self.render_to_response(context)

    def create_api_key(self, form):
        prefix, api_key, api_hash_key = generate_api_key()
        form.instance.id = prefix
        form.instance.api_token = api_hash_key
        form.instance.user = self.request.user
        form.save()
        return api_key

    def get_object_api(self):
        try:
            return ApiKeyModel.objects.get(
                user=self.request.user, is_deleted=False, is_expired=False
            )
        except ObjectDoesNotExist:
            return False


class ApiKeyDeleteView(LoginRequiredMixin, DeleteView):
    model = ApiKeyModel
    success_url = reverse_lazy("api-key-view")
    template_name = "api_key/api_key_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super(ApiKeyDeleteView, self).get_context_data(**kwargs)
        context["block_update_but"] = check_limit(self.request.user.pk)
        return context

    def get_object(self, queryset=None):
        queryset = self.model.objects.filter(user=self.request.user)
        return super().get_object(queryset)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.is_expired = True
        self.object.save()
        api_delete_limit_check(self.request.user.pk)
        return HttpResponseRedirect(success_url)
