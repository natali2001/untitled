import unittest
from django.conf.urls import url, include
from django.contrib import admin
from antipyretic import views


urlpatterns = [
 url(r'^antipyretic/$', views.antipyretic, name='antipyretic'),
]
