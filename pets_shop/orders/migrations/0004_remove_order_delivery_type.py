# Generated by Django 4.2.7 on 2024-04-10 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_delivery_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_type',
        ),
    ]
