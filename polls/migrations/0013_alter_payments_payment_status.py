# Generated by Django 4.0.1 on 2022-03-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_remove_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]