from django import forms

from profiles.models import UserProfile, Addresses, UserSocialMedia


class UserProfileForms(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }


class AddressesForms(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = '__all__'
        exclude = ['user']


class UserSocialMediaForms(forms.ModelForm):
    class Meta:
        model = UserSocialMedia
        fields = '__all__'
        exclude = ['user']
