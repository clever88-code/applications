from django.shortcuts import render, redirect
from core.models import Application, Status, Labs_cabinets, office
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from core.filters import get_filters, get_sortings

@login_required
def applications_by_status(request):

    statuses = [2, 5]

    sortings = get_sortings(request)
    filters = get_filters(request)

    if 'status_application' in filters:
        statuses.append(filters['status_application'])

    print(statuses)
    applications = Application.objects.filter(
        Q(status_application__in=statuses)
        &
        Q(
            **dict(list(filters.items()))
        )
    ).order_by(sortings['ascing'] + sortings['sorting'])

    statuses = Status.objects.all()
    cabinets = office.objects.all()

    return render(
        request,
        'labs_admin_applications.html',
        {
            'applications': applications,
            'current_sorting': sortings['sorting'],
            'current_ascing': sortings['current_ascing'],
            'statuses': statuses,
            'filters': filters,
            'cabinets': cabinets,
        }
    )


@login_required
def edit_application(request, application_id):
    if request.method == 'POST':
        application = Application.objects.get(id=application_id)
        application.status_application = Status.objects.get(id=5)
        application.worker = request.user
        application.save()
       
    return redirect('/labs_admin_applications/')


@login_required
def archive_application(request, application_id):
    if request.method == 'POST':
        application = Application.objects.get(id=application_id)
        application.status_application = Status.objects.get(id=3)
        application.worker = request.user
        application.save()
       
    return redirect('/labs_admin_applications/')

@login_required
def return_application(request, application_id):
    if request.method == 'POST':
        application = Application.objects.get(id=application_id)
        application.status_application = Status.objects.get(id=4)
        application.comments = request.POST.get('comments')
        application.worker = request.user
        application.save()
       
    return redirect('/labs_admin_applications/')