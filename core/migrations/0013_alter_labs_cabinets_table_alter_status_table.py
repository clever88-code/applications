# Generated by Django 4.2.6 on 2023-10-21 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_labs_cabinets'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='labs_cabinets',
            table='labs_cabinets',
        ),
        migrations.AlterModelTable(
            name='status',
            table='statuses',
        ),
    ]