from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import doorLog

def index(request):
    latest_log_list = doorLog.objects.order_by('-log_timestamp')[:5]
    template = loader.get_template('door/index.html')
    context = {'latest_log_list': latest_log_list}
    return render(request, 'door/index.html', context)
