from django.db import models

# Create your models here.




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




class office(models.Model):
    number = models.CharField('Номера кабинета', default="", max_length=9)

    class Meta:
        #managed = False
        db_table = 'office'
        verbose_name = 'кабинет'
        verbose_name_plural = 'кабинеты'

    def __str__(self):
        return f'{self.number}'
    

class application(models.Model):
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    number_cab = models.ForeignKey(office, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Выберите кабинет')
    description = models.TextField('Описание проблемы')

    class Meta:
        #managed = False
        db_table = 'application'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.date}'


