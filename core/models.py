from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        #managed = False
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return f'{self.name}'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'
    def __str__(self):
        return f'{self.username}'



class office(models.Model):
    number = models.CharField('Номера кабинета', default="", max_length=9)

    class Meta:
        #managed = False
        db_table = 'offices'
        verbose_name = 'кабинет'
        verbose_name_plural = 'кабинеты'

    def __str__(self):
        return f'{self.number}'
    

class Application(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name = 'Дата и Время')
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Преподователь')
    number_cab = models.ForeignKey(office, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Выберите кабинет')
    description = models.TextField('Описание проблемы')
    status_application = models.ForeignKey(Status, on_delete=models.CASCADE, default='1', verbose_name = 'Cтатус')
    worker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'groups__name': 'labs'},  # Фильтр для выбора только пользователей из группы 'labs'
        verbose_name = 'Лаборант' 
    )
    comments = models.TextField('Комментарии',  null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        #managed = False
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'№{self.id} каб.{self.number_cab} Заявитель {self.auth_user}'
    

    def change_status(self, new_status):
        if self.status_application != new_status:
            self.status_application = new_status
            self.history_user = User  # Устанавливаем пользователя, который изменил статус  
            self.save()



class Labs_cabinets(models.Model):
    cabinet = models.ForeignKey(office, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Кабинет лаборанта')
    worker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'groups__name': 'labs'},  # Фильтр для выбора только пользователей из группы 'labs'
        verbose_name = 'Лаборант' 
    )

    class Meta:
        #managed = False
        db_table = 'labs_cabinets'
        verbose_name = 'Кабинеты лаборатов'
        verbose_name_plural = 'Кабинеты лаборатов'
    def __str__(self):
        return f'Кабинет {self.cabinet} привязан к лаборату {self.worker}'

