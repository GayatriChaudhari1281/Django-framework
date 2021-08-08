"""FifthProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from demo import views

urlpatterns = [
    url(r'^d1/', views.display1_view),
    url(r'^d2/', views.display2_view),
    url(r'^d3/', views.display3_view),
    url(r'^d4/', views.display4_view),
    url(r'^d5/', views.display5_view),
]
# Now includes(link) all these urls at project level
