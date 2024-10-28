from django.contrib.auth.models import AbstractUser
from django.db import models

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

