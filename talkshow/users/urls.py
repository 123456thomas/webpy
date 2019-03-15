# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^userinfo/$',views.userinfo),
    url(r'^$',views.index),
]