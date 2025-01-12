from django import template
from django.utils.translation import get_language
from preferences.models import WebsiteOwner
from preferences.templatetags.local_data import convert_number_to_persian
from extensions.utils import persian_week_days, english_week_days
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.simple_tag
def owner_full_name():
    try:
        website_owner = WebsiteOwner.objects.first()
        return website_owner.owner.get_full_name()
    except:
        return _("Owner Name")


@register.simple_tag
def owner_phone_number_fa():
    try:
        website_owner = WebsiteOwner.objects.first()
        return convert_number_to_persian(website_owner.owner.phone_number)
    except:
        return _("Owner Phone Number")


@register.simple_tag
def owner_phone_number_en():
    try:
        website_owner = WebsiteOwner.objects.first()
        return website_owner.owner.phone_number
    except:
        return _("Owner Phone Number")


@register.simple_tag
def owner_email():
    try:
        website_owner = WebsiteOwner.objects.first()
        return website_owner.owner.email
    except:
        return _("Owner Email")

@register.simple_tag
def owner_work_time():
    try:
        website_owner = WebsiteOwner.objects.first()
        if get_language() == "en":
            work_days = f'{english_week_days(website_owner.start_work_day)} - {english_week_days(website_owner.end_work_day)}: '
            work_time = f'{website_owner.strat_work_time.strftime("%H:%M")} - {website_owner.end_work_time.strftime("%H:%M")}'
        else:
            work_days = f'{persian_week_days(website_owner.start_work_day)} تا {persian_week_days(website_owner.end_work_day)}: '
            work_time = convert_number_to_persian(f'از {website_owner.strat_work_time.strftime("%H:%M")} تا {website_owner.end_work_time.strftime("%H:%M")}')
        return work_days + work_time
    except:
        return _("Owner Work Time")


@register.simple_tag
def owner_address():
    try:
        website_owner = WebsiteOwner.objects.first()
        address = website_owner.owner.addresses.get_address()
    except:
        address = _("Owner Address ")
    return address
