from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'null': True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.CharField(max_length=150, verbose_name='Почта', help_text='Введите почту', unique=True)

    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Введите номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatar', verbose_name='Фото', help_text='Загрузите фото', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', help_text='Укажите страну', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.email}'

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Укажите пользователя', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', help_text='Укажите курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', help_text='Укажите урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты', help_text='Укажите сумму оплаты', **NULLABLE)
    payment_method = models.CharField(max_length=20, choices={"Cash": "Наличные", "Non_cash": "Перевод на счет"}, verbose_name="Способ оплаты", help_text="Выберите способ оплаты", **NULLABLE)
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
