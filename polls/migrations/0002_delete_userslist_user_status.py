# Generated by Django 4.0.1 on 2022-02-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userslist',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
