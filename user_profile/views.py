from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, FormView

from user_profile.forms import RegistrationForm, EditForm


class RegisterView(FormView):
    template_name = "user_profile/register.html"
    form_class = RegistrationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        return render(self.request, "user_profile/register_done.html", {"new_user": new_user})


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
