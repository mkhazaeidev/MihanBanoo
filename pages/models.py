from django.db import models
from preferences.patterns import SingletonModel
from django.utils.translation import gettext_lazy as _, get_language


class PhotoSlider(models.Model):
    en_title = models.CharField(max_length=100, verbose_name=_("English title"))
    fa_title = models.CharField(max_length=100, verbose_name=_("Persian title"))
    image = models.ImageField(upload_to='slider/', verbose_name=_("Image"),
                              help_text=_("Used to display in the background of a slide."))
    en_text = models.TextField(verbose_name=_("English text"))
    fa_text = models.TextField(verbose_name=_("Persian text"))
    order = models.SmallIntegerField(verbose_name=_("Display order"),
                                     help_text=_("Specify the slide display order, which slide should be the first."))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title if get_language() == 'en' else self.fa_title

    class Meta:
        verbose_name = _('PhotoSlider')
        verbose_name_plural = _('PhotoSliders')


class AboutUs(SingletonModel):
    en_title = models.CharField(max_length=200, verbose_name=_("English title"),
                                help_text=_("For display in database tables only. The main title is in the section title section."))
    fa_title = models.CharField(max_length=200, verbose_name=_("Persian title"),
                                help_text=_("For display in database tables only. The main title is in the section title section."))
    en_description = models.TextField(verbose_name=_("English description"))
    fa_description = models.TextField(verbose_name=_("Persian description"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title if get_language() == 'en' else self.fa_title

    class Meta:
        verbose_name = _('AboutUs')
        verbose_name_plural = _('AboutUs')


class Services(models.Model):
    en_title = models.CharField(max_length=200, verbose_name=_("English title"))
    fa_title = models.CharField(max_length=200, verbose_name=_("Persian title"))
    en_description = models.TextField(verbose_name=_("English description"))
    fa_description = models.TextField(verbose_name=_("Persian description"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title if get_language() == 'en' else self.fa_title

    class Meta:
        verbose_name = _('Services')
        verbose_name_plural = _('Services')
