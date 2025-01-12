from django.db import models
from preferences.patterns import SingletonModel
from django.utils.translation import gettext_lazy as _


class PhotoSlider(models.Model):
    en_title = models.CharField(max_length=100, verbose_name='عنوان انگلیسی اسلاید')
    fa_title = models.CharField(max_length=100, verbose_name='عنوان فارسی اسلاید')
    image = models.ImageField(upload_to='slider/', verbose_name='تصور اسلاید',
                              help_text='برای نمایش در پس زمینه اسلاید استفاده می شود.')
    en_text = models.TextField(verbose_name='متن انگلیسی اسلاید')
    fa_text = models.TextField(verbose_name='متن فارسی اسلاید')
    order = models.SmallIntegerField(verbose_name='ترتیب نمایش',
                                     help_text='ترتیب نمایش اسلاید را مشخص کنید که چندمین اسلاید باشد.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title

    class Meta:
        verbose_name = _('PhotoSlider')
        verbose_name_plural = _('PhotoSliders')


class AboutUs(SingletonModel):
    en_title = models.CharField(max_length=200, verbose_name='عنوان انگلیسی',
                                help_text='فقط برای نمایش در جداول دیتابیس. عنوان اصلی در بخش عنوان بخشها می باشد')
    fa_title = models.CharField(max_length=200, verbose_name='عنوان فارسی',
                                help_text='فقط برای نمایش در جداول دیتابیس. عنوان اصلی در بخش عنوان بخشها می باشد')
    en_description = models.TextField(verbose_name='متن انگلیسی درباره ما')
    fa_description = models.TextField(verbose_name='متن فارسی درباره ما')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title

    class Meta:
        verbose_name = _('AboutUs')
        verbose_name_plural = _('AboutUs')
