# Generated by Django 5.2 on 2025-05-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_car_image_alter_car_profit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['-expense_date']},
        ),
    ]
