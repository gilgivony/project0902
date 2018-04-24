from django.contrib.auth.mixins import LoginRequiredMixin
from .models import entry,worker_report
from django.db.models import Count, Sum, Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import getpass
import psycopg2
import calendar
import datetime



conn = psycopg2.connect(r'postgresql://postgres@localhost:5432/')
cur = conn.cursor()


now = datetime.datetime.now()


class FOB_EntriesListView(ListView):

    def get_queryset(self):
        user = str.lower(getpass.getuser())
        # user = 'olaf_v'

        month_passed = int(self.kwargs['pk'])

        # All the records from FOB + ADP + Calendar for the entire month
        queryset = entry.objects.filter( # Records of the entire month
            (Q(user_name__contains=user, month_work=month_passed)|Q(user_name='', month_work=month_passed)))\
            .order_by('work_day','-gross_minutes_at_work').distinct('work_day')

        # queryset = entry.objects.filter(
        #     (Q(user_name__contains=user, month_work=month_passed)|Q(user_name='', month_work=month_passed))& Q(work_day__lt=now))\
        #     .order_by('work_day','-gross_minutes_at_work').distinct('work_day')

        return queryset

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    template_name = 'fob/hours.html'
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def get_context_data(self, **kwargs):
        user = str.lower(getpass.getuser())
        # user = 'olaf_v'

        month_passed = int(self.kwargs['pk'])
        context = super(FOB_EntriesListView, self).get_context_data(**kwargs)
        context['today'] =  datetime.date(2018, month_passed, now.day)
        context['year']= now.year
        context['Month'] = str(calendar.month_name[month_passed]) # bring month name

        # All the records related to the userename from FOB + ADP
        qs_real_values = entry.objects.filter(
            (Q(user_name__contains=user, month_work=month_passed)))

        # qs_real_values = entry.objects.filter(
        #    (Q(user_name__contains=user, month_work=month_passed))& Q(work_day__lt=now))

        qs_bp = qs_real_values.filter(source_of_records='BP') # Select only the records from Business Portal
        qs_fob = qs_real_values.filter(source_of_records='FOB') # Select only the records from FOB (ADP is counted as reported)
        qs_adp = qs_real_values.filter(source_of_records='ADP') # Select only the records from FOB as a seperate record
        qs_user = qs_real_values.filter(source_of_records='USER') # Select only the records from FOB as a seperate record
        qs_fob_and_adp = qs_real_values.filter(Q(source_of_records='ADP') |
                                               Q(source_of_records='FOB') |
                                               Q(source_of_records='USER'))  # All FOB records + ADP  + USER records.

        worker_name = str(qs_real_values.values('worker')[0].values()) # bring the first directory. it will bri
        worker_name = worker_name.split("['")[1].split("']")[0] # Clean string
        context['worker'] = worker_name # Tag it as 'worker'

        # days_at_work = qs_fob.aggregate(Count('user_name'))
        days_at_work = qs_fob_and_adp.aggregate(Count('user_name')) # Count the days reported as FOB or ADP

        total_minutes_reported = qs_fob_and_adp.aggregate(Sum('net_minutes_at_work')) # FOB + ADP in minutes

        context['total_minutes_reported']=total_minutes_reported

        # Check if there are reports from ADP
        try:
            total_minutes_adp = qs_adp.aggregate(Sum('net_minutes_at_work'))
            adp_hours = int(str(total_minutes_adp.values()).split('[')[1].split(']')[0]) / 60
        except:
            adp_hours=0

        context['total_minutes_adp'] = adp_hours

        # Check if there are reports from USER
        try:
            total_minutes_user = qs_user.aggregate(Sum('net_minutes_at_work'))
            user_hours = int(str(total_minutes_user.values()).split('[')[1].split(']')[0]) / 60
        except:
            user_hours=0

        context['total_minutes_user'] = user_hours

        reported_hours = int(str(total_minutes_reported.values()).split('[')[1].split(']')[0])/60

        if  adp_hours==0:
            fob_hours = int(str(total_minutes_reported.values()).split('[')[1].split(']')[0])/60# Total hours from FOB/60

        else:
            fob_hours = reported_hours - adp_hours


        reported_hours = int(str(total_minutes_reported.values()).split('[')[1].split(']')[0])/60

        total_bp_hours = qs_bp.aggregate(Sum('BP_hours'))
        total_bp_hours = str(total_bp_hours.values()).split('[')[1].split(']')[0]
        context['BP_HOURS'] = total_bp_hours # Located above BP Hours title

        context['fob_hours'] = "{0:.2f}".format(fob_hours)
        context['reported_hours'] = "{0:.2f}".format(reported_hours)
        context['FOB_days'] = int(str(days_at_work.values()).split('[')[1].split(']')[0])

        return context

# import floppyforms as forms
#
# class DatePicker(forms.DateInput):
#     template_name = 'datepicker.html'
#
#     class Media:
#         js = (
#             'js/jquery.min.js',
#             'js/jquery-ui.min.js',
#         )
#         css = {
#             'all': (
#                 'css/jquery-ui.css',
#             )
#         }


# class AddRecord(CreateView):
#     model = worker_report
#     fields = ['work_day', 'user_comment', 'hours']
