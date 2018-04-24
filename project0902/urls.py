from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from form import views as core_views



urlpatterns = [
    url(r'^files/', include('db_file_storage.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='form/home.html'), name='home'), # LALALAL
    # url(r'^login/$', auth_views.login, {'template_name': 'form/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'form/logged_out.html'}, name='logout'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^form/', include('form.urls')),
    url(r'^fob/', include('fob.urls')),
]

