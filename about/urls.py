import unittest
from django.conf.urls import url, include
from django.contrib import admin
from about import views


urlpatterns = [
 url(r'^about/$', views.about, name='about'),
]
