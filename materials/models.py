from django.db import models

from config import settings


NULLABLE = {'null': True, "blank": True}


class Course(models.Model):
    course_name = models.CharField(max_length=30, verbose_name='Название курса', help_text='Введите название курса', **NULLABLE)
    preview = models.ImageField(upload_to='materials/preview', verbose_name='Фото', help_text='Загрузите фото', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Заполните описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Создатель курса', help_text='Укажите создателя курса', **NULLABLE)

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=30, verbose_name='Название урока', help_text='Введите название урока')
    description = models.TextField(verbose_name='Описание', help_text='Заполните описание', **NULLABLE)
    preview = models.ImageField(upload_to='materials/preview', verbose_name='Фото', help_text='Загрузите фото', **NULLABLE)
    video = models.CharField(max_length=500, verbose_name='Ссылка на видео', help_text='Загрузите видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, help_text='Укажите курс', verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Создатель урока',
                              help_text='Укажите создателя урока', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)
    email_date = models.DateTimeField(**NULLABLE, verbose_name='Дата сообщения об изменении')

    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'



