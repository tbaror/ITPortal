from django import forms
from .models import MainTask


class TaskCraetionForm(forms.form):
    
    class Meta:
        fields = ['task_title',
            'global_task_info',
            'due_date',
            'global_task_assign',
            'task_status',
        
        ]