# Generated by Django 4.2.6 on 2023-10-16 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_status_remove_application_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status_application',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
    ]