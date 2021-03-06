# Generated by Django 4.0.1 on 2022-02-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
