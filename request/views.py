
from django.shortcuts import render, redirect
from django.views.generic import FormView
import asyncio
from .forms import application
# Create your views here.
class RecordView(FormView):
    template_name = 'record.html'
    form_class = application
    success_url = '/record'


def add_orders(request):
    if request.POST:
        form = application(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()


    return redirect('/record/')
