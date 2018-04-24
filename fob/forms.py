from django import forms
#
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import worker_report
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField



# class AddRecord(CreateView):
#     model = worker_report
#     fields = ['work_day', 'user_comment', 'hours']
#
#     def get_form(self, form_class):
#         form = super(AddRecord, self).get_form(form_class)
#         form.fields['work_day'].widget = forms.SelectDateWidget(years=2018)
#         return form

class AddForm(forms.ModelForm):
    class Meta:
        model = worker_report
        fields = ['work_day', 'user_comment', 'hours']
        my_field = DateField(widget=AdminDateWidget)
        widgets = {
            'work_day': forms.SelectDateWidget
        }

class AddRecord(CreateView):
    form_class = AddForm
    model = worker_report

