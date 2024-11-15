import json
import smtplib
from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.db.models.functions import datetime
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from config.settings import EMAIL_HOST_USER
from materials.models import Lesson
from users.models import User


@shared_task
def send_change_subs(data_name, email_list):
    """ Отправка сообщения об изменении подписки """
    print('Отправка сообщения об изменении подписки')
    try:
        send_mail(
            subject=f'Изменения в: {data_name}',
            message=f'Сообщаем Вам, в подписке произошли изменения',
            from_email=EMAIL_HOST_USER,
            recipient_list=email_list,
        )
    except smtplib.SMTPException as server_response:
        print(server_response)


@shared_task
def check_last_login():
    """ Для периодической проверки последнего входа """
    print("Проверка last_login")
    date = datetime.datetime.now()
    users = User.objects.all()
    for user in users:
        print(user.last_login)
        if user.last_login:
            if user.last_login > user.last_login + timedelta(days=30):
                user.is_active = False
        else:
            if user.last_login > user.date_joined + timedelta(days=30):
                user.is_active = False


@shared_task
def check_update_lesson():
    """ Проверяем наличие изменений за последние 4 часа. И если изменения были, отправляем письма """
    print("Проверяем наличие изменений за последние 4 часа")
    date = datetime.datetime.now()
    lesson = Lesson.objects.all()
    email_list = []
    for les in lesson:
        if date > les.email_date + timedelta(hours=4) and date > les.updated_ta + timedelta(hours=4):
            les.email_date = date
            email_list.append(les.owner.email)
    send_mail(
        subject=f'Произошли изменения в: {les.lesson_name}',
        message=f'Ознакомьтесь с изменениями {les.description}',
        from_email=EMAIL_HOST_USER,
        recipient_list=email_list
    )
