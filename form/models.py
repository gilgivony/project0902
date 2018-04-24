from django.contrib.auth.models import User
from datetime import datetime

from db_file_storage.model_utils import delete_file, delete_file_if_needed
from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=150,default='')

    def __str__(self):
        return self.task_name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=250, default=None)
    manufacturer_code= models.CharField(max_length=3, default=None)

    def __str__(self):
        return self.manufacturer_code + ' - ' + self.manufacturer_name

class Jurisdiction(models.Model):
    jurisdiction_name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.jurisdiction_name

FEATURED = (
    (0,'No'),
    (1, 'Everywhere'),
    (2, 'category-only')
)
class Technical_Manager(models.Model):
    manager_full_name = models.CharField(max_length=250, blank=True, default=None)
    manager_email = models.EmailField(max_length=50)
    manager_name = models.CharField(max_length=100)
    still_working = models.BooleanField(default=False)
    # featured = models.IntegerField(choices=FEATURED, default=0)
    # categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.manager_full_name


class DevRep(models.Model):
    devrep_full_name = models.CharField(max_length=250, null=True)
    devrep_email = models.EmailField(max_length=50)
    devrep_name = models.CharField(max_length=100)


    def __str__(self):
        return self.devrep_full_name

class Type_of_work(models.Model):
    type_of_work = models.CharField(max_length=30,  default='',blank=True)

    def __str__(self):
        return self.type_of_work

class Request_status(models.Model):
    Request_status = models.CharField(max_length=30,  default='',blank=True)

    def __str__(self):
        return self.Request_status

class Contact_details(models.Model):
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=None, default=None)
    contact_name = models.CharField(max_length=250, default=None)
    contact_email = models.EmailField(max_length=150, default=None)
    contact_telephone = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.contact_name


class manufarturer_billing_details(models.Model):
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=None, default=None)
    manufarturer_billing_name = models.CharField(max_length=250, default=None)
    manufarturer_billing_contact_name = models.CharField(max_length=250, default=None)
    manufarturer_billing_address = models.CharField(max_length=250, default=None)
    manufarturer_billing_city = models.CharField(max_length=250, default=None)
    manufarturer_billing_POBox = models.CharField(max_length=250, default=None)
    manufarturer_billing_country = models.CharField(max_length=250, default=None)
    manufarturer_billing_tax = models.CharField(max_length=250, default=None)
    manufarturer_billing_phone = models.CharField(max_length=250, default=None)

    def __str__(self):
        return  self.contact_name

class Opportunity(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    Opportunity_name = models.CharField(max_length=200, default=None)
    general_description = models.TextField(max_length=3000, default=None)
    request_status = models.ForeignKey(Request_status, on_delete=models.CASCADE, default='')
    Technical_Manager = models.ForeignKey(Technical_Manager, on_delete=models.CASCADE, default=None)
    devrep = models.ForeignKey(DevRep, on_delete=models.CASCADE, default=None)
    jurisdiction = models.ForeignKey(Jurisdiction, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(default=datetime.now,blank=True)
    contact_name = models.ForeignKey(Contact_details, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField('Task', through='OpportunityTask')
    type_of_work = models.ForeignKey(Type_of_work,on_delete=None, default=None)
    file1 = models.FileField(upload_to='form.OpportunityFile/bytes/filename/mimetype', blank=True, null=True)
    file2 = models.FileField(upload_to='form.Opportunityfile/bytes/filename/mimetype', blank=True, null=True)
    # contact_name = models.TextField(default=None)


    def __str__(self):
        return str(self.id) + ' '+ self.Opportunity_name

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'file1')
        delete_file_if_needed(self, 'file2')
        super(Opportunity, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Opportunity, self).delete(*args, **kwargs)
        delete_file(self, 'file1')
        delete_file(self, 'file2')

class OpportunityTask(models.Model):
    task = models.ForeignKey(Task, on_delete=None)
    opportunity = models.ForeignKey(Opportunity, on_delete=None)
    hours = models.FloatField(default=0)

class OpportunityFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=150)
#
#
# class Console(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     # picture = models.ImageField(upload_to='form.ConsolePicture/bytes/filename/mimetype', blank=True, null=True)
#     pig = models.FileField(upload_to='form.ConsolePicture/bytes/filename/mimetype', blank=True, null=True)
#     pig2 = models.FileField(upload_to='form.ConsolePicture/bytes/filename/mimetype', blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         delete_file_if_needed(self, 'pig')
#         delete_file_if_needed(self, 'pig2')
#         super(Console, self).save(*args, **kwargs)
#
#     def delete(self, *args, **kwargs):
#         super(Console, self).delete(*args, **kwargs)
#         delete_file(self, 'pig')
#         delete_file(self, 'pig2')