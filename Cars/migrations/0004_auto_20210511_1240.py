# Generated by Django 3.1.1 on 2021-05-11 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_auto_20210511_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car_engine',
            options={'verbose_name_plural': 'car Engine'},
        ),
        migrations.AlterModelOptions(
            name='contact_dealer',
            options={'verbose_name_plural': 'Contact Dealer'},
        ),
    ]