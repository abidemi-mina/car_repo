# Generated by Django 3.2 on 2021-05-21 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_cars_car_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='car_img',
            new_name='car_image',
        ),
    ]