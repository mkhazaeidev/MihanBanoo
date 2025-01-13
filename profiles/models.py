from django.db import models
from django.urls import reverse
from accounts.models import User
from extensions.utils import jalali_convertor
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    GENDER = (
        ('m', _("Male")),
        ('f', _("Female")),
        ('o', _("Other")),
    )

    MARRIAGE = (
        ('m', _("Married")),
        ('s', _("Single")),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_("User"),
        related_name='profile',
    )
    avatar = models.ImageField(
        upload_to='users/profile/avatar/',
        blank=True,
        null=True,
        verbose_name=_("Avatar"),
    )
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True, verbose_name=_("Gender"))
    birthday = models.DateField(blank=True, null=True, verbose_name=_("Birthday"))
    marriage = models.CharField(max_length=1, choices=MARRIAGE, blank=True, null=True, verbose_name=_("Marriage"))
    education = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Education"))
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Job"))
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles:index')

    def jalali_birthday(self):
        return jalali_convertor(self.birthday)

    jalali_birthday.short_description = _("Birthday")

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")


class UserSocialMedia(models.Model):
    APP_NAME_CHOICES = (
        ('linkedin', 'LinkedIn'),
        ('telegram', 'Telegram'),
        ('facebook', 'Facebook'),
        ('youtube', 'Youtube'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('twitter', 'Twitter'),
        ('skype', 'Skype'),
        ('github', 'GitHub'),
        ('pinterest', 'Pinterest'),
        ('snapchat-ghost', 'Snapchat'),
        ('reddit', 'Reddit'),
        ('google', 'Google'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User Name"), related_name='social_media')
    app_name = models.CharField(
        max_length=15, blank=True, null=True, choices=APP_NAME_CHOICES, verbose_name=_("Application Name")
    )
    qrcode = models.ImageField(upload_to='users/profile/SocialMediaQRCode/', blank=True, null=True,
                               verbose_name='QR Code')
    link = models.CharField(max_length=400, blank=True, null=True, verbose_name=_("Link"))
    username = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Username"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name.title()

    class Meta:
        verbose_name = _("User Social Media Profile")
        verbose_name_plural = _("User Social Media Profiles")


class Addresses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User Name"), related_name='addresses')
    country = models.CharField(max_length=30, blank=True, null=True, default=_("Iran"), verbose_name=_("Country"))
    province = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Province"))
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("City"))
    main_st = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Main Street"))
    auxiliary_st = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Auxiliary Street"))
    street_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Street"))
    building_number = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Building Number"))
    building_unit_number = models.CharField(max_length=30, blank=True, null=True,
                                            verbose_name=_("Building Unit Number"))
    postal_code = models.CharField(max_length=10, blank=True, null=True, verbose_name=_("Postal Code"))
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Phone Number"))

    def __str__(self):
        return self.user.username

    def get_address(self):
        address = []
        if self.province:
            address.append(self.province)
        elif self.city:
            address.append(self.city)
        elif self.main_st:
            address.append(self.main_st)
        elif self.auxiliary_st:
            address.append(self.auxiliary_st)
        elif self.street_name:
            address.append(self.street_name)
        elif self.building_number:
            address.append(self.building_number)
        elif self.building_unit_number:
            address.append(self.building_unit_number)

        if len(address) < 2:
            return ''.join(address)
        else:
            return ' - '.join(address)

    class Meta:
        verbose_name = _("User Address")
        verbose_name_plural = _("User Addresses")
