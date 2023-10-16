from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import RecordView, add_orders, DeleteApplicationView
from . import views
app_name = "request"

urlpatterns = [
    path('', RecordView.as_view(), name="record"),
    path('add_orders', add_orders, name="add_orders"),
    path('delete_application/<int:application_id>/', DeleteApplicationView.as_view(), name="delete_application"),
]