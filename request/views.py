
from django.shortcuts import render, redirect
from django.views.generic import FormView
import asyncio

# Create your views here.
class OrderFormView(FormView):
    template_name = 'orders.html'
    form_class = OrderForm
    success_url = '/record'


def add_orders(request):
    if request.POST:
        form = OrderForm(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()


    return redirect('/record/')