from django.contrib import admin
# from .models import  Opportunity,Jurisdiction,  Technical_Manager,Manufacturer, Contact_details, Request_status

from . import  models
admin.site.register(models.worker_report)

@admin.register(models.entry)
class FOB_Entries(admin.ModelAdmin):
    list_display = ['worker','work_day','first_entry', 'last_entry']

    fields = (
        ('worker','team'),
        ('work_day','month'),
        ('first_entry', 'last_entry')
    )