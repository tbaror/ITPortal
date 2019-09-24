from django.shortcuts import render, redirect
#from .models import List
#from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request ,'index.html', {})
    