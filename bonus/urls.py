"""vh5000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='index'),
    path('index/', views.index, name='index'),
    path('how/', views.how, name='how'),  
    path('about/', views.about, name='about'),
    path('connect/', views.connect, name='connect'),  
    path('recommend/',views.recommend,name='recommend'),
    path('prizes/', views.PrizeListView.as_view()),
    path('prizes/<int:pk>', views.PrizeDetailView.as_view(), name='prize-detail'),
    path('heart/',views.heartamount),
]

