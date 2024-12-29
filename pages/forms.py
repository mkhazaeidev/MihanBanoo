from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import get_language


language = get_language()


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=200, label='', widget=forms.TextInput(attrs={
        'placeholder': "Name" if language == "en" else "نام",
        'class': 'form-control',
    }))
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={
        'placeholder': "Email" if language == "en" else "ایمیل",
        'class': 'form-control',
    }), validators=[EmailValidator()])
    subject = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={
        'placeholder': "Subject" if language == "en" else "موضوع",
        'class': 'form-control',
    }))
    message = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={
        'placeholder': "Message" if language == "en" else "متن پیام",
        'class': 'form-control',
        'rows': '5',
    }))
