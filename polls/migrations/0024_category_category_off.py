# Generated by Django 4.0.1 on 2022-03-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_remove_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_off',
            field=models.IntegerField(default=0),
        ),
    ]