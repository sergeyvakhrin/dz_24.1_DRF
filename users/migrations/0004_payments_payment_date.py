# Generated by Django 5.1.2 on 2024-10-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments_payment_date_alter_payments_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата оплаты'),
        ),
    ]