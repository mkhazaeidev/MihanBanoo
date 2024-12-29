from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
        exclude = ['user', 'groups', 'user_permissions']
        widgets = {
            'username': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'type': 'email', 'class': 'form-control'}
            ),
            'phone_number': forms.TextInput(
                attrs={'type': 'phone', 'class': 'form-control'}
            ),
        }
