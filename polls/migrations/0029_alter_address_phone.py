# Generated by Django 4.0.1 on 2022-04-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_alter_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
