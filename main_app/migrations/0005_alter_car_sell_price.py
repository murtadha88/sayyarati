# Generated by Django 5.2 on 2025-05-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car_sell_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='sell_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
