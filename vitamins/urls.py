import unittest
from django.conf.urls import url, include
from django.contrib import admin
from vitamins import views


urlpatterns = [
 url(r'^vitamins/$', views.vitamins, name='vitamins'),
]