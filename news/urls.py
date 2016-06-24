from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from . import views

urlpatterns = [
		url(r'^$',views.index, name = 'index'),
		]


