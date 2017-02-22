from django.conf.urls import urllib

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
