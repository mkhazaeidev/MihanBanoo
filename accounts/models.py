from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=False, unique=True)

    def get_fullname(self):
        return super().get_full_name()

    get_fullname.short_description = "Name"

    def __str__(self):
        return self.get_fullname() + f'({self.username})'

    def get_absolute_url(self):
        return reverse('accounts:dashboard')
