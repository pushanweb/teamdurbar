# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 00:54:45 2021

@author: Pushan
"""

from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
]