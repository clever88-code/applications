
from django.shortcuts import render, redirect
from django.views.generic import FormView
import asyncio

from django.views import View
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import Application_forms  # Замените YourFormClass на имя вашего класса формы
from core.models import Application  # Используйте правильное имя модели
from django.views import View


class RecordView(FormView):
    template_name = 'record.html'
    form_class = Application_forms
    success_url = '/record'
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user_applications = Application.objects.filter(auth_user_id=user_id)
        form = Application_forms
        context = {
            'user_applications': user_applications,
            'form': form,
        }
        return render(request, self.template_name, context)
def add_orders(request):
    if request.POST:
        form = Application_forms(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()


    return redirect('/record/')


class DeleteApplicationView(View):
    def post(self, request, application_id):
        try:
            application = Application.objects.get(id=application_id)
            if application.auth_user_id == request.user.id:
                application.delete()
                print(f"Заявка {application_id} удалена успешно.") 
        except Application.DoesNotExist:
            pass
        return redirect('request:record')