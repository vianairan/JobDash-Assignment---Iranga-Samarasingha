# -*- coding: utf-8 -*-
"""
Created on Jan 27 2014
@author: Iranga Samarasingha
"""
from django.conf.urls import patterns, url

from todo_app import views

urlpatterns = patterns('',
    url(r'^$', views.Index, name='index'),
)