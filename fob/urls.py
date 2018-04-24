from django.conf.urls import url
from fob.forms import AddRecord
from .views import FOB_EntriesListView
app_name = 'fob'

urlpatterns = [
    url(r'^(?P<pk>\d+)$', FOB_EntriesListView.as_view(), name='user_hours'),
    url(r'add_record/$',AddRecord.as_view(),name='add-record'),
]
