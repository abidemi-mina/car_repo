# Generated by Django 3.2 on 2021-05-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0008_alter_car_type_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_name',
            field=models.CharField(max_length=200),
        ),
    ]
