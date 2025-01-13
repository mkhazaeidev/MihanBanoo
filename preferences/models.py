from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from preferences.patterns import SingletonModel
from accounts.models import User


class WebsiteDetails(SingletonModel):
    page_title_en = models.CharField(
        max_length=100,
        verbose_name=_("English Page Title"),
        blank=True,
        help_text=_("The name that appears at the top of the page as the title.")
    )

    page_title = models.CharField(
        max_length=100,
        verbose_name=_("Page Title"),
        blank=True,
        help_text=_("The name that appears at the top of the page as the title.")
    )

    main_title_en = models.CharField(
        max_length=200,
        verbose_name=_("English Main Title"),
        blank=True,
        help_text=_("The name that is used as the main name of the site or as the site logo.")
    )

    main_title = models.CharField(
        max_length=200,
        verbose_name=_("Main Title"),
        blank=True,
        help_text=_("The name that is used as the main name of the site or as the site logo.")
    )

    logo_image = models.ImageField(
        upload_to='website/images/logo/',
        blank=True,
        null=True,
        verbose_name=_("Logo Image")
    )

    logo_touch_icon = models.ImageField(
        upload_to='website/images/logo/',
        blank=True, null=True,
        verbose_name=_("Logo Touch icon")
    )

    description = models.CharField(
        max_length=400,
        verbose_name=_("Description"),
        blank=True,
        help_text=_("A brief explanation of the goals of the site.")
    )
    seo_keyword = models.CharField(
        max_length=400,
        verbose_name=_("SEO Keywords"),
        blank=True,
        help_text=_("Keywords to help Google search engine.")
    )

    def __str__(self):
        return self.page_title

    def get_absolute_url(self):
        return reverse('accounts:dashboard')

    class Meta:
        verbose_name = _("Website Details")
        verbose_name_plural = _("Website Details")


class WebsiteOwner(SingletonModel):
    WEEK_DAYS = (
        ('1', _("Saturday")),
        ('2', _("Sunday")),
        ('3', _("Monday")),
        ('4', _("Tuesday")),
        ('5', _("Wednesday")),
        ('6', _("Thursday")),
        ('7', _("Friday")),
    )
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Website Owner"),
    )

    start_work_time = models.TimeField(
        verbose_name=_("Start work time"),
        blank=True,
        null=True
    )

    end_work_time = models.TimeField(
        verbose_name=_("End work time"),
        blank=True,
        null=True
    )

    start_work_day = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=WEEK_DAYS,
        verbose_name=_("The first working day of the week")
    )

    end_work_day = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=WEEK_DAYS,
        verbose_name=_("Last working day of the week")
    )

    def __str__(self):
        return self.owner.get_full_name()

    def get_absolute_url(self):
        return reverse('accounts:dashboard')

    class Meta:
        verbose_name = _('Website Owner')
        verbose_name_plural = _('Website Owner')


class Titles(models.Model):
    SECTIONS = (
        ('about', _("About")),
        ('services', _("Services")),
        ('contact', _("Contact")),
        ('footer', _("Footer")),
    )

    section = models.CharField(max_length=10, choices=SECTIONS, verbose_name=_("Section Name"), unique=True)
    en_title = models.CharField(max_length=50, verbose_name=_("English Title"))
    fa_title = models.CharField(max_length=50, verbose_name=_("Persian Title"))
    en_subtitle = models.CharField(max_length=400, blank=True, verbose_name=_("English Subtitle"))
    fa_subtitle = models.CharField(max_length=400, blank=True, verbose_name=_("Persian Subtitle"))

    def __str__(self):
        return self.get_section_display()

    class Meta:
        verbose_name = _("Titles")
        verbose_name_plural = _("Titles")
