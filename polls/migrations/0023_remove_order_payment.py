# Generated by Django 4.0.1 on 2022-03-20 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
    ]
