# Generated by Django 4.0.1 on 2022-02-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_product_image2_product_image3_product_image4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]