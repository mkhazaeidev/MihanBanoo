from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(
        blank=False,
        unique=True,
        verbose_name=_("Phone number")
    )

    def get_fullname(self):
        return super().get_full_name()

    get_fullname.short_description = _("Name")

    def __str__(self):
        return f"{self.get_fullname()} ({self.username})"

    def get_absolute_url(self):
        return reverse('accounts:dashboard')
