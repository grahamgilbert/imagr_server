import json
import requests
from django.conf import settings
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
        if settings.SLACK_NOTIFY:
            try:
                notify_slack_channel(serial, message, status)
            except:
                return HttpResponse('Error sending slack notification')
        return HttpResponse(data)


def notify_slack_channel(serial, message, status):
    text = "%s %s %s" % (serial, status, message)
    url = settings.SLACK_WEBHOOK_URL
    channel = settings.SLACK_CHANNEL
    user = settings.SLACK_BOT_NAME
    emoji =''
    headers = {'content-type':'application/json'}
    payload = json.dumps({
        'channel' : channel,
        'username' : user,
        'text' : text,
        'icon_emoji' : emoji,
        })
    request = requests.post(url, headers=headers, data=payload)
