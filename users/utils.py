from django.conf import settings
from django.core.mail import send_mail

from django.utils.translation import gettext_lazy as _



def send_email(subject, message, to):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to])

def send_activation_code(to, code):
    subject = _('Code email de verification')
    message = _(f'Votre email code est - {code}')
    send_email(subject, message, to)

def send_reset_password_code(to, code):
    subject = 'code de reinitialisation'
    message = f'Vote code de reinitialisation est -  {code}'
    send_email(subject, message, to)