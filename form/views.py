from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Opportunity
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import forms
from .models import Technical_Manager,Jurisdiction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from form.forms import SignUpForm



# http://127.0.0.1:8000/form/all_opp
class All_opportunitiesListView(LoginRequiredMixin, ListView):
    queryset = Opportunity.objects.all()
    template_name = 'form/index.html'

    # http://127.0.0.1:8000/form/<pk>/
class OpportunitiesDetailView(DetailView):
    template_name = 'form/detail.html'
    queryset = Opportunity.objects.all()

    def get_context_data(self,**kwargs):
        context = super(OpportunitiesDetailView,self).get_context_data(**kwargs)
        return context


class CreateOpportunity(CreateView):

    model = Opportunity
    fields = [
        'request_status',
        'Technical_Manager',
        'jurisdiction',
        'Opportunity_name',
        'contact_name'
    ]
    template_name = 'form/form_opportunity.html'

class UpdateOpportunity(UpdateView):
    model = Opportunity
    fields = [
        'request_status',
        'Technical_Manager',
        'jurisdiction',
        'Opportunity_name',
        'contact_name'
    ]
    template_name = 'form/form_opportunity.html'

@login_required
def home(request):
    return render(request, 'home.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


