from django.conf.urls import url
from form.views import  All_opportunitiesListView, OpportunitiesDetailView, CreateOpportunity, UpdateOpportunity
app_name = 'form'

urlpatterns = [
    # url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^opportunity/(?P<pk>[0-9]+)/$', UpdateOpportunity.as_view(), name='opportunity-update'),

    url(r'^opportunity/add/$', CreateOpportunity.as_view(), name='opportunity-add'),
    url(r'^all_opp', All_opportunitiesListView.as_view(),name='view_all'),
    url(r'^(?P<pk>[0-9]+)$', OpportunitiesDetailView.as_view(), name='request-detail'),

]

