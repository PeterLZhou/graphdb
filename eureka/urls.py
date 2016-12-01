from django.conf.urls import patterns, url, include
from eureka import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^graph', views.graph, name='graph'))
