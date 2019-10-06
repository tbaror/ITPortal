from django.shortcuts import render
from django.urls import path
from ittasks.views import IndexView

# Create your views here.
urlpatterns = [
    #path('',views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
]