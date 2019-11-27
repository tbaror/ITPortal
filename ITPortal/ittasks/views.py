from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import MainTask, ChildTask, User 
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone


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
        #filter active runing tasks
        context['active_tasks'] = MainTask.objects.filter(complete=False).count()
        #All oobjects main Task
        context['maintask'] = MainTask.objects.all()

        
        
        #filter task due date
        #due_range = 
        context['due_task'] = MainTask.objects.filter(due_date__day__lte=7, complete=False).count()
        context['due_task_obj'] = MainTask.objects.filter(due_date__day__lte=7, complete=False)
        #task paused
        context['task_paused'] = MainTask.objects.filter(task_status='PA', complete=False).count()
       
        #task paused
        context['task_completed'] = MainTask.objects.filter(task_status='CO', complete=True).count()

        #task paused
        context['task_started'] = MainTask.objects.filter(task_status='NS', complete=True).count()

        ###query for dashboard
        #recent tasks query
        context['recent_task'] = MainTask.objects.filter(created_at__gte=datetime.now()-timedelta(days=30), complete=False)

        #Current date time
        now = timezone.now()
        context['current_time'] = now

        #Recent task update
        context['recent_updates'] = MainTask.objects.filter(updated_at__gte=datetime.now()-timedelta(days=7), complete=False)

        #All objects Subtask
        
        #context['usersubtask'] = ChildTask.objects.get(id=1)

        
        return context
        
class TaskView(TemplateView):
    template_name = "tasks_view.html"
    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)

        context['objtasks'] = MainTask.objects.all()
        return context
