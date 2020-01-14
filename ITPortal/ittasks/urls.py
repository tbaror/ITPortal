from django.shortcuts import render
from django.urls import path
from ittasks.views import IndexView , TaskView, CreatTaskView, LoaderPage, UpdateListTaskView, TaskIdUpdateView

# Create your views here.
urlpatterns = [
    #path('',views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path("task_view/", TaskView.as_view(), name="task_view"),
    path("create_task/", CreatTaskView.as_view(), name="create_task"),
    path("update_task/", UpdateListTaskView.as_view(), name="update_task"),
    path("loader_page/", LoaderPage.as_view(), name="loader_page"),
    path("<int:pk>/", TaskIdUpdateView.as_view(), name="taskid_update"),

    

]