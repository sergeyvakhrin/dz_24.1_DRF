import smtplib

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_change_subs(subscription_name, email_list):
    """ Отправка сообщения об изменении подписки """

    try:
        send_mail(
            subject=f'Изменения в подписке: {subscription_name}',
            message=f'Сообщаем Вам, в подписке произошли изменения',
            from_email=EMAIL_HOST_USER,
            recipient_list=email_list,
        )
    except smtplib.SMTPException as server_response:
        print(server_response)