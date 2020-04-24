import unittest
from django.conf.urls import url, include
from django.contrib import admin
from nerves import views


urlpatterns = [
 url(r'^nerves/$', views.nerves, name='nerves'),
]