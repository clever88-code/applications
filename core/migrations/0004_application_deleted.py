# Generated by Django 4.2.6 on 2023-10-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_application_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='deleted',
            field=models.BooleanField(default=True),
        ),
    ]
