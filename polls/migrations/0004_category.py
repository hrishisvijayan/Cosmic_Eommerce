# Generated by Django 4.0.1 on 2022-02-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
    ]