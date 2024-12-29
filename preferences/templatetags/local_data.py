from django.utils.translation import get_language
from django import template
from django.utils.timezone import localtime
from extensions.utils import persian_number_convertor, jalali_convertor

register = template.Library()

@register.simple_tag
def language():
    return get_language()
    

@register.filter
def convert_number_to_persian(number):
    number = str(number)
    if number.startswith('+'):
        number = number[1:]
        number = persian_number_convertor(number)
        number = '+' + number
    else:
        number = persian_number_convertor(number)

    return number


@register.filter
def date_to_persian(date):
    return jalali_convertor(date)


@register.filter
def time_to_persian(utc_date_time):
    local_date_time = localtime(utc_date_time)
    time = local_date_time.time().strftime("%H:%M")
    return convert_number_to_persian(time)

