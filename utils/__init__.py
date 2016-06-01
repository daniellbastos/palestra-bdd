from datetime import datetime, timedelta
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.utils import timezone


class EmailFromTemplate(EmailMultiAlternatives):
    def __init__(self, subject='', from_email=settings.DEFAULT_FROM_EMAIL, to=None, template_name=None, context={}, **kwargs):
        if template_name is None:
            raise TypeError('You must specify a template base name')

        context['site_name'] = settings.SITE_NAME
        context['site_domain'] = settings.SITE_DOMAIN
        context['STATIC_URL'] = settings.STATIC_URL

        text_template = template_name + '.txt'
        text_content = render_to_string(text_template, context)
        super(EmailFromTemplate, self).__init__(subject, text_content, from_email, to, **kwargs)

        html_template = template_name + '.html'
        html_content = render_to_string(html_template, context)
        self.attach_alternative(content=html_content, mimetype='text/html')


def get_date_of_current_week(weekday):
    """
    Returns an instance of datetime with the weekday of the current week.
    """
    monday = timezone.now()
    if monday.weekday() > 1:
        monday = monday - timedelta(days=monday.weekday())
    return get_date_of_week(weekday, monday)


def get_date_of_week(weekday, monday):
    """
    TODO
    """
    if weekday <= 5:
        date = monday + timedelta(days=weekday)
    else:
        date = monday - timedelta(days=1)

    return datetime(date.year, date.month, date.day)


def get_monday(date):
    if date.weekday() == 6:
        monday = date + timedelta(days=1)
    else:
        if date.weekday() == 1:
            monday = date
        else:
            monday = date - timedelta(days=date.weekday())
    return monday


def check_intersect_dates(start1, end1, start2, end2):
    """
    Returns True when date1 intersect with the date2.
    """
    return (start1 <= start2 < end1) or (start1 < end2 <= end1)
