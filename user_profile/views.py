from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from user_profile.forms import EditForm


class UpdateViewProfile(LoginRequiredMixin, UpdateView):
    template_name = "user_profile/edit_profile.html"
    model = User
    form_class = EditForm
    success_url = reverse_lazy("edit")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Данные были успешно изменены")
        return super().form_valid(form)
