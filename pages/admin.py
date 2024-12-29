from django.contrib import admin
from pages.models import PhotoSlider


@admin.register(PhotoSlider)
class PhotoSliderAdmin(admin.ModelAdmin):
    list_display = ['en_title', 'order']
    list_filter = ['en_title', ]
    ordering = ['order', 'en_title']