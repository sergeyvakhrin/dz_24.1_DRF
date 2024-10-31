import json
from datetime import datetime
from pathlib import Path
from django.db import connection
from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):

    def load_data(self) -> list[dict]:
        """ Метод для загрузки данных из json """
        ROOT_PATH = Path(__file__).parent.parent.parent.parent
        DATA_PATH = ROOT_PATH.joinpath('payments.json')
        with open(DATA_PATH, 'rt', encoding="UTF-8") as file:
            payments = json.load(file)
        return payments

    def get_patmants(self, payments) -> list:
        """ Метод для получения списка экземпляров Класса Payment для заполнения базы данных """
        payments_for_create = []
        for item in payments:
            data = item['fields']
            if item['model'] == 'users.payments':
                payments_for_create.append(Payments(
                    pk=item['pk'],
                    user=User.objects.get(pk=data['user']),
                    paid_course=Course.objects.get(pk=data['paid_course']),
                    paid_lesson=Lesson.objects.get(pk=data['paid_lesson']),
                    payment_amount=data.get('payment_amount', 0),
                    payment_method=data.get('payment_method', 'Cash'),
                    payment_date=data.get('payment_date', None)
                ))
        return payments_for_create

    def handle(self, *args, **options) -> None:
        """ Метод автоматически срабатывает при обращении к коменде fill """

        print("Загрузка данных")
        payments = self.load_data()

        print("Очистка Базы данных")
        Payments.objects.all().delete()


        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE users_payments RESTART IDENTITY CASCADE;')


        print("Создание Платежей")
        payments_for_create = self.get_patmants(payments)
        Payments.objects.bulk_create(payments_for_create)

