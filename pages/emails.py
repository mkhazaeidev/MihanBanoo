from django.core.mail import send_mail
from preferences.models import WebsiteOwner
from django.contrib import messages

from django.utils.translation import get_language


language = get_language()


def send_email(request, valid_data):
    website_owner = WebsiteOwner.objects.first()
    email_text = {
        'Name': valid_data["name"],
        'Email': valid_data["email"],
        'Subject': valid_data["subject"],
        'Message': valid_data['message'],
    }
    message = ''
    for key, value in email_text.items():
        message += key + ':\n\t' + f' {value}' + '\n'

    try:
        send_mail(
            subject="Contact us" if language == "en" else 'ارتباط با ما',
            from_email=email_text['Email'],
            recipient_list=[website_owner.owner.email],
            message=message
        )
        messages.success(
            request,
            'Your message was sent successfully.' if language == "en" else 'پیام شما با موفقیت ارسال شد.'
        )
    except:
        messages.error(
            request,
            'Your message was not sent.' if language == "en" else 'پیام شما ارسال نشد.'
        )
