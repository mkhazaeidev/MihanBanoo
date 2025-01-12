from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import admin
from django.apps import apps
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_list = []

        # Iterate through all installed apps
        for app in apps.get_app_configs():
            models = []
            for model in app.get_models():
                if model in admin.site._registry:
                    model_admin = admin.site._registry[model]
                    model_info = {
                        'model': model,
                        'model_name': _(model._meta.verbose_name),
                        'app_label': _(model._meta.app_label),
                        'add_url': reverse(f'admin:{model._meta.app_label}_{model._meta.model_name}_add'),
                        'change_url': reverse(f'admin:{model._meta.app_label}_{model._meta.model_name}_change',
                                              args=[1]),  # Example ID
                    }
                    models.append(model_info)

            if models:
                app_list.append({
                    'name': _(app.verbose_name),
                    'label': _(app.label),
                    'models': models,
                })
        context['app_list'] = app_list
        return context


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(auth_views.LogoutView):
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy("accounts:password_change_done")


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy("accounts:password_reset_done")


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password_reset_complete")
    template_name = "accounts/password_reset_confirm.html"


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
