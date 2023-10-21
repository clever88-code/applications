# Generated by Django 4.2.6 on 2023-10-21 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_alter_application_auth_user_alter_application_worker_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalApplication',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и Время')),
                ('description', models.TextField(verbose_name='Описание проблемы')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('auth_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.authuser', verbose_name='Преподователь')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('number_cab', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.office', verbose_name='Выберите кабинет')),
                ('status_application', models.ForeignKey(blank=True, db_constraint=False, default='1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.status', verbose_name='Cтатус')),
                ('worker', models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'groups__name': 'labs'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Лаборант')),
            ],
            options={
                'verbose_name': 'historical Заявка',
                'verbose_name_plural': 'historical Заявки',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
