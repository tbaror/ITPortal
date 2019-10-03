from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import MainTask, ChildTask 
#from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request ,'index.html', {})



""" class HomePageView(ListView):

    template_name = "index.html"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context = MainTask.objects.all()
        return context """

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['active_tasks'] = MainTask.objects.filter(complete=False).count()
        context['maintask'] = MainTask.objects.all()
        #context['categories'] = Category.objects.all()
        #context['comments'] = Comments.objects.all()
        return context    