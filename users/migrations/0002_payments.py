# Generated by Django 5.1.2 on 2024-10-30 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_lesson_course'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.IntegerField(blank=True, help_text='Укажите сумму оплаты', null=True, verbose_name='Сумма оплаты')),
                ('payment_method', models.CharField(blank=True, choices=[('N', 'Наличные'), ('С', 'Перевод на счет')], help_text='Выберите способ оплаты', max_length=1, null=True, verbose_name='Способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, help_text='Укажите курс', null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Курс')),
                ('paid_lesson', models.ForeignKey(blank=True, help_text='Укажите урок', null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='Урок')),
                ('user', models.ForeignKey(blank=True, help_text='Укажите пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
    ]
