# Generated by Django 4.2.6 on 2023-10-16 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_car_application_number_cab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='date',
        ),
    ]