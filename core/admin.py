from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html

admin.site.register(office)
#admin.site.register(Status)
admin.site.register(Labs_cabinets)

class ApplicationAdmin(SimpleHistoryAdmin):
    history_list_display = ['Дата', 'Преподаватель', 'Кабинет', 'Статус', 'Коммент']

    def Дата(self, obj):
        return obj.date
    
    def Преподаватель(self, obj):
        return obj.auth_user
        
    def Кабинет(self, obj):
        return obj.number_cab
    
    def Статус(self, obj):
        return obj.status_application
        
    def Коммент(self, obj):
        return obj.comments

    # history_list_display = ["changed_fields", "list_changes"]
    
    # def changed_fields(self, obj):
    #     fields = ApplicationAdmin.get_fields()
    #     if obj.prev_record:
    #         delta = obj.diff_against(obj.prev_record)
    #         change_fields = []
    #         for field in delta.changed_fields:
    #             change_fields.append(fields[field])
    #         return change_fields
    #     return None

    # def list_changes(self, obj):
    #     fields = ApplicationAdmin.get_fields()
    #     fieldsText = ""
    #     if obj.prev_record:
    #         delta = obj.diff_against(obj.prev_record) 

    #         for change in delta.changes:
    #             fieldsText += str("<strong>{}</strong> изменено с <span style='background-color:#ffb5ad'>{}</span> на <span style='background-color:#b3f7ab'>{}</span> . <br/>".format(fields[change.field], change.old, change.new))
    #         return format_html(fieldsText)
    #     return None
    
    # def get_fields():
    #     return {
    #         'date': 'Дата',
    #         'auth_user': 'Пользователь',
    #         'number_cab': 'Номер кабинета',
    #         'status_application': 'Статус',
    #         'comments': 'Комментарии',
    #         'worker': 'Лаборант',
    #         'description': 'Описание проблемы',
    #     }


admin.site.register(Application, ApplicationAdmin)





