from django.conf.urls import patters, urls
from rango import views

urlpatters = patterns('',
                      url(r'^$', views.index, name='index'))