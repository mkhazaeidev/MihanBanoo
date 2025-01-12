from django.contrib import admin
from preferences.models import *
from pages.models import AboutUs


@admin.register(WebsiteDetails)
class WebsiteDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(WebsiteOwner)
class WebsiteOwnerAdmin(admin.ModelAdmin):
    pass


# @admin.register(BackgroundImages)
# class BackgroundImagesAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Titles)
# class TitlesAdmin(admin.ModelAdmin):
#     list_display = ['section', 'title', 'description']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['en_title']