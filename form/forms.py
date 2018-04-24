from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class CreateOpportunity(forms.ModelForm):
    class Meta:
        model = models.Opportunity
        fields = '__all__'



class CreateOpportunityForm(forms.ModelForm):
    class Meta:
        model = models.Opportunity
        fields = '__all__'



# Sign Up With Extra Fields
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
