from django.contrib import admin
from profiles.models import UserProfile, Addresses, UserSocialMedia


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birthday', 'marriage')
    list_filter = ('gender', 'birthday', 'marriage')


@admin.register(Addresses)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'province', 'city', 'postal_code')
    list_filter = ('country', 'province', 'city', 'postal_code')


@admin.register(UserSocialMedia)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'app_name', 'username')
    list_filter = ('user__username', 'app_name')
