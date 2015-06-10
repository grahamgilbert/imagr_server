from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext, loader
from django.db.models import Max
from datetime import datetime

from report.models import *

# Create your views here.
@login_required
def index(request):
    new_today = Computer.objects.filter(date_added__lte=datetime.today())

    computers = Computer.objects.all()

    in_progress = []
    errors = []
    completed = []

    for computer in computers:
        if computer.current_status == 'in_progress':
            in_progress.append(computer)
        elif computer.current_status == 'error':
            error.append(computer)
        elif computer.current_status == 'success':
            completed.append(computer)
    c = {'new_today':new_today, 'in_progress':in_progress, 'errors':errors, 'completed':completed}
    return render(request, 'dashboard/index.html', c)

def new_computers_today(request):
    computers = Computer.objects.filter(date_added__lte=datetime.today()).annotate(last_seen=Max('report__date_added'))
    c = {'computers':computers, 'list_title':'New Machines Today'}
    return render(request, 'dashboard/list.html', c)

def in_progress(request):
    computers = Computer.objects.filter(current_status='in_progress').annotate(last_seen=Max('report__date_added'))
    c = {'computers':computers, 'list_title':'In Progress'}
    return render(request, 'dashboard/list.html', c)

def error(request):
    computers = Computer.objects.filter(current_status='error').annotate(last_seen=Max('report__date_added'))
    c = {'computers':computers, 'list_title':'Errors'}
    return render(request, 'dashboard/list.html', c)

def completed(request):
    computers = Computer.objects.filter(current_status='success').annotate(last_seen=Max('report__date_added'))
    c = {'computers':computers, 'list_title':'Completed'}
    return render(request, 'dashboard/list.html', c)

def info(request, computer_serial):
    computer = get_object_or_404(Computer, serial_number=computer_serial)
    reports = computer.report_set.all()
    c = {'computer':computer, 'reports':reports}
    return render(request, 'dashboard/info.html', c)
