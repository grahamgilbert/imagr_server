from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
# Create your views here.
@csrf_exempt
def index(request):
    data = request.POST
    serial = data['serial']
    message = data['message']
    status = data['status']
    # see if the computer exists
    if serial:
        try:
            computer = Computer.objects.get(serial_number=serial)
        except Computer.DoesNotExist:
            computer = Computer(serial_number=serial)
        computer.current_status = status    
        computer.save()

        # create a new report object
        report = Report(computer=computer, message=message, status=status)
        report.save()
        return HttpResponse(data)
