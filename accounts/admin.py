from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Personal Information', {
            'fields': ('phone_number',)}),
        ('Permissions',
         {
             "fields": (
                 'is_superuser',
                 'is_staff',
                 'is_active',
             ),
         },),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        'username', User.get_full_name, 'email', 'phone_number', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
    )

