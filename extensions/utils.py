from . import jalali


def persian_number_convertor(number):
    numbers = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    for en_number, fa_number in numbers.items():
        number = number.replace(en_number, fa_number)
    return number


def persian_week_days(day):
    week_days = {
        '1': 'شنبه',
        '2': 'یک شنبه',
        '3': 'دوشنبه',
        '4': 'سه شنبه',
        '5': 'چهار شنبه',
        '6': 'پنج شنبه',
        '7': 'جمعه',
    }
    for en_day, fa_day in week_days.items():
        day = day.replace(en_day, fa_day)
    return day


def english_week_days(day):
    week_days = {
        '1': 'Saturday',
        '2': 'Sunday',
        '3': 'Monday',
        '4': 'Tuesday',
        '5': 'Wednesday',
        '6': 'Thursday',
        '7': 'Friday',
    }
    for en_day, fa_day in week_days.items():
        day = day.replace(en_day, fa_day)
    return day


def jalali_month_name(month):
    jalai_month = ['فرودین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    return str(jalai_month[month - 1])


def jalali_convertor(date):
    date_to_str = f'{date.year},{date.month},{date.day}'
    date_to_tuple = jalali.Gregorian(date_to_str).persian_tuple()

    output = f'{date_to_tuple[2]} {jalali_month_name(date_to_tuple[1])} {date_to_tuple[0]}'
    return persian_number_convertor(output)
