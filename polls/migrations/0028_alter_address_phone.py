# Generated by Django 4.0.1 on 2022-04-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_offer_remove_category_category_name_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
