from django.utils.translation import get_language, gettext_lazy as _

from django import template
from preferences.models import WebsiteDetails

register = template.Library()


@register.simple_tag
def website_page_title():
    try:
        website_details = WebsiteDetails.objects.first()
        if get_language() == 'en':
            return website_details.page_title_en
        else:
            return website_details.page_title
    except:
        return _("Website Page Name")


@register.simple_tag
def website_main_title():
    try:
        website_details = WebsiteDetails.objects.first()
        if get_language() == 'en':
            return website_details.main_title_en
        else:
            return website_details.main_title
    except:
        return _("Website Title")


@register.simple_tag
def website_logo_image():
    try:
        website_details = WebsiteDetails.objects.first()
        return website_details.logo_image.url
    except:
        return _("Website Logo Image")


@register.simple_tag
def website_description():
    try:
        website_details = WebsiteDetails.objects.first()
        return website_details.description
    except:
        return _("Website Description")


@register.simple_tag
def website_seo_keyword():
    try:
        website_details = WebsiteDetails.objects.first()
        return website_details.seo_keyword
    except:
        return _("Website Seo Keyword")