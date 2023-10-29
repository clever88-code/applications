def get_sortings(request):
    sorting = '-id'
    ascing = ''
    current_ascing = 1

    if request.POST.get('sorting') != None:
        sorting = request.POST.get('sorting')
    if request.POST.get('ascing') != None and request.POST.get('ascing') == '0':
        ascing = '-'
        current_ascing = 0

    return {
        'sorting': sorting,
        'ascing': ascing,
        'current_ascing': current_ascing
    }

def get_filters(request):
    filters = {}

    if request.POST.get('date_filter') != '' and request.POST.get('date_filter') != None:
        filters['date__contains'] = request.POST.get('date_filter')
    if request.POST.get('status_application') != None and request.POST.get('status_application') != '0':
        filters['status_application'] = int(request.POST.get('status_application'))
    if request.POST.get('number_cab') != None and request.POST.get('number_cab') != '0':
        filters['number_cab'] = int(request.POST.get('number_cab'))


    return filters