from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^check_email/$', views.check_email),
]
