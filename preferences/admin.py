from django.contrib import admin
from preferences.models import *
from django.utils.translation import get_language


@admin.register(WebsiteDetails)
class WebsiteDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(WebsiteOwner)
class WebsiteOwnerAdmin(admin.ModelAdmin):
    pass


# @admin.register(BackgroundImages)
# class BackgroundImagesAdmin(admin.ModelAdmin):
#     pass


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['section', 'en_title', 'en_subtitle'] if get_language() == 'en' else ['section', 'fa_title', 'fa_subtitle']
