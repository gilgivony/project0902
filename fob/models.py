from django.db import models
import getpass
from django.urls import reverse

import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.conf import settings
from datetime import datetime

class entry(models.Model):
    class Meta:
        app_label='fob'
        db_table = 'fob_entry'

    team = models.CharField(max_length=150,blank=True)
    worker = models.CharField(max_length=150, default=None, null=False)
    user_name = models.CharField(max_length=150, default='')
    work_day = models.DateField()
    first_entry = models.CharField(max_length=5)
    last_entry = models.CharField(max_length=5)
    gross_minutes_at_work = models.IntegerField(null=True)
    net_minutes_at_work = models.IntegerField(null=True)
    gross_time_at_work = models.CharField(max_length=5)
    net_time_at_work = models.CharField(max_length=5,default='')
    time_reported = models.CharField(max_length=5,default='')
    BP_hours  = models.FloatField()
    month_work = models.IntegerField()
    adp_comments = models.CharField(max_length=100, default='')
    source_of_records = models.CharField(max_length=100, default='')
    day_name = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.worker + '   ' + str(self.work_day)

today = datetime.today()
month_number = today.month


class worker_report(models.Model):


    class Meta:
        app_label = 'fob'
        db_table = 'worker_report'

    LIST_OF_OPTIONS = (
        ('Business trip','Business trip'),
        ('Work from home', 'Work from home')
    )

    work_day = models.DateField()
    user_comment = models.CharField(max_length=50,
                               choices=LIST_OF_OPTIONS,
                               default='')
    hours = models.FloatField()
    user_name = models.CharField(max_length=50,default=str.lower(getpass.getuser()))

    def __str__(self):
        return str(self.work_day) + '     ' + str(self.user_comment) + '      ' + str(self.hours) + ' hours'

    def get_absolute_url(self):
        return u'/fob/'+ str(month_number)