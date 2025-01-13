from django.contrib import admin
from pages.models import PhotoSlider, AboutUs, Services
from django.utils.translation import get_language


@admin.register(PhotoSlider)
class PhotoSliderAdmin(admin.ModelAdmin):
    list_display = ['en_title', 'order'] if get_language() == 'en' else ['fa_title', 'order']
    list_filter = ['en_title'] if get_language() == 'en' else ['fa_title']
    ordering = ['order', 'en_title'] if get_language() == 'en' else ['order', 'fa_title']

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['en_title'] if get_language() == 'en' else ['fa_title']
    list_filter = ['en_title'] if get_language() == 'en' else ['fa_title']
    ordering = ['en_title'] if get_language() == 'en' else ['fa_title']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['en_title'] if get_language() == 'en' else ['fa_title']
    list_filter = ['en_title'] if get_language() == 'en' else ['fa_title']
    ordering = ['en_title'] if get_language() == 'en' else ['fa_title']
