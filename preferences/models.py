from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from preferences.patterns import SingletonModel
from accounts.models import User


# class WebsiteDetails(SingletonModel):
#     en_page_title = models.CharField(max_length=100, verbose_name='عنوان انگلیسی سایت', blank=True,
#                                      help_text='نامی که در بالای صفحه به عنوان تایتل نمایش داده می شود.')
#     fa_page_title = models.CharField(max_length=100, verbose_name='عنوان فارسی سایت', blank=True)
#     en_main_title = models.CharField(max_length=200, verbose_name='نام انگلیسی سایت', blank=True,
#                                      help_text='نامی که به عنوان اسم سایت و یا به عنوان لوگوی سایت استفاده می شود.')
#     fa_main_title = models.CharField(max_length=200, verbose_name='نام فارسی سایت', blank=True)
#     logo_image = models.ImageField(upload_to='website/images/logo/', blank=True, null=True, verbose_name='تصویر لوگو')
#     logo_touch_icon = models.ImageField(upload_to='website/images/logo/', blank=True, null=True,
#                                         verbose_name='تصویر آیکون لوگو')
#     en_description = models.CharField(max_length=400, blank=True, verbose_name='شرح انگلیسی سایت',
#                                       help_text='توضیح مختصری راجع به اهداف سایت')
#     fa_description = models.CharField(max_length=400, blank=True, verbose_name='شرح فارسی سایت')
#     seo_keyword = models.CharField(max_length=400, blank=True, verbose_name='کلمات کلیدی برای سئو',
#                                    help_text='کلمات کلیدی برای کمک به موتور جستجوگر گوگل')
#
#     def __str__(self):
#         return self.en_page_title
#
#     def get_absolute_url(self):
#         return reverse('accounts:dashboard')
#
#     class Meta:
#         verbose_name = 'مشخصات وب سایت'
#         verbose_name_plural = 'مشخصات وب سایت'


class WebsiteOwner(SingletonModel):
    WEEK_DAYS = (
        ('1', 'شنبه'),
        ('2', 'یک شنبه'),
        ('3', 'دوشنبه'),
        ('4', 'سه شنبه'),
        ('5', 'چهار شنبه'),
        ('6', 'پنج شنبه'),
        ('7', 'جمعه'),
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='مالک سایت',
                                 help_text='انتخاب مالک سایت از بین کاربران برای نمایش اطلاعات تماس.')
    strat_work_time = models.TimeField(verbose_name='ساعت شروع کار', blank=True, null=True)
    end_work_time = models.TimeField(verbose_name='ساعت پایان کار', blank=True, null=True, )
    start_work_day = models.CharField(max_length=1, choices=WEEK_DAYS, verbose_name='اولین روز کاری در هفته',
                                      blank=True, null=True)
    end_work_day = models.CharField(max_length=1, choices=WEEK_DAYS, verbose_name='آخرین روز کاری در هفته', blank=True,
                                    null=True)

    def __str__(self):
        return self.owner.get_full_name()

    def get_absolute_url(self):
        return reverse('accounts:dashboard')

    class Meta:
        verbose_name = _('WebsiteOwner')
        verbose_name_plural = _('WebsiteOwner')
