from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import MainTask, ChildTask, User, UserProfile 
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Count, Q
from .forms import *
from django.urls import reverse_lazy
from django.forms import inlineformset_factory





class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #filter active runing tasks
        context['active_tasks'] = MainTask.objects.filter(complete=False).count()
        #All oobjects main Task
        context['maintask'] = MainTask.objects.all()
        #IT Team
        context['usermaintask'] = UserProfile.objects.all().annotate(user_task=Count('global_task_assign'))
        #context['countusr'] = MainTask.objects.values_list('global_task_assign')
        context['usrmtsk'] = MainTask.objects.filter(complete=False).annotate(num_task=Count('global_task_assign')).annotate(ts_complete=Count('complete')).filter(complete=True)
        #context['usrobj']= UserProfile.objects.annotate(numtask=Count('global_task_assign'))
        context['usrobj'] = UserProfile.objects.annotate(complete=Count('global_task_assign__complete'
                           , filter=Q(global_task_assign__complete=True)), paused=Count('global_task_assign__task_status'
                           , filter=Q(global_task_assign__task_status = "PA"))
                           ,num_ts=Count('global_task_assign'))
                           
        #context['usrobj'] = UserProfile.objects.filter(global_task_assign__task_status = "PA").annotate(numtask=Count('global_task_assign'))
        
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

class LoaderPage(TemplateView):
    template_name = 'loader_page.html'
    def get_context_data(self, **kwargs):
        context = super(LoaderPage, self).get_context_data(**kwargs)
        context ['lobj'] = MainTask.objects.all()[:1]
              
        
class TaskView(TemplateView):
    template_name = "tasks_view.html"
    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)

        context['objtasks'] = MainTask.objects.all()
        return context


class CreatTaskView(CreateView):
    model = MainTask

    template_name = "create_newtask.html"
    form_class = TaskCraetionForm
    success_url = reverse_lazy('loader_page')

class UpdateListTaskView(TemplateView):
    #model = MainTask
    template_name = "update_task.html"
    #form_class = TaskUpdateForm

    def get_context_data(self, **kwargs):
            context = super(UpdateListTaskView, self).get_context_data(**kwargs)
            #current tasks
            context['cur_tasks'] = MainTask.objects.filter(complete=False)
            return context

class TaskIdUpdateView(UpdateView):
    taskidformset = inlineformset_factory(MainTask,ChildTask, fields=('task_description','task_info','task_complete',
    'sub_task','task_precent_complete','task_due_date','task_assign'))
    model = MainTask
    template_name = "taskid_update.html"
    form_class = TaskUpdateForm
    