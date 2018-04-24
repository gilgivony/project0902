from django.contrib import admin
# from .models import  Opportunity,Jurisdiction,  Technical_Manager,Manufacturer, Contact_details, Request_status

from . import  models
admin.site.register(models.Opportunity)

admin.site.register(models.Jurisdiction)
admin.site.register(models.Request_status)
admin.site.register(models.Manufacturer)
admin.site.register(models.Contact_details)
admin.site.register(models.Category)
admin.site.register(models.Task)
admin.site.register(models.DevRep)
admin.site.register(models.Type_of_work)



class OpportunityItemInline(admin.TabularInline):
    model = models.OpportunityTask

@admin.register(models.Technical_Manager)
class Technical_Manager(admin.ModelAdmin):
    list_display = ['manager_full_name', 'manager_email', 'manager_name', 'still_working']
    ordering = ['manager_full_name']
    # list_filter = ['manager_name']
    list_editable = ['still_working']
    # search_fields = ['manager_name']
    fields = (
        ('manager_full_name', 'still_working'),
        ('manager_email','manager_name')
        #  , 'featured'),
        # ('categories')
              )
    # filter_horizontal = ['categories']
    # radio_fields = {'featured': admin.HORIZONTAL}

# @admin.register(models.Opportunity)
# class Opportunity(admin.ModelAdmin):
#     inlines = [OpportunityItemInline]
#     list_display = ['owner','id', 'Opportunity_name', 'created_at']
#     fields = (
#         'Opportunity_name', 'jurisdiction', 'Technical_Manager','contact_name','request_status','owner',
#         'file1', 'file2'
#     )

# from .models import Console
#
# from db_file_storage.form_widgets import DBAdminClearableFileInput
# from django import forms
# from django.contrib import admin
#
# class ConsoleForm(forms.ModelForm):
#     class Meta:
#         model = Console
#         exclude = []
#         widgets = {
#             'picture': DBAdminClearableFileInput
#         }
#
# class ConsoleAdmin(admin.ModelAdmin):
#     form = ConsoleForm