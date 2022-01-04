from django.urls import path
from . import views
# from django.conf.urls.defaults import patterns, include, url

urlpatterns = [
    path('', views.f, name='index'),
]