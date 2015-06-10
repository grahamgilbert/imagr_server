from django.db import models
from datetime import datetime

# Create your models here.

class Computer(models.Model):
    serial_number = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(max_length=200)
    def __str__(self):
        return self.serial_number

    class Meta:
      get_latest_by = 'date_added'

class Report(models.Model):
    computer = models.ForeignKey(Computer)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=512)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s - %s - %s" % (self.date_added, self.computer, self.status)

    class Meta:
      get_latest_by = 'date_added'
      ordering = ['-date_added']
