from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(\d*)$', views.index),
    url(r'^share/(\d)/(\d*)$', views.share),
    url(r'^note/(\d*)$', views.note),
    url(r'^life/(\d*)$', views.life),
    url(r'^about/$', views.about),
    url(r'^detail/(\d+)/$', views.detail),
]