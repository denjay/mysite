from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^share/(\d)$', views.share),
    url(r'^note/$', views.note),
    url(r'^life/$', views.life),
    url(r'^about/$', views.about),
    url(r'^detail/(\d+)/$', views.detail),
]