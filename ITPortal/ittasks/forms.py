from django import forms
from .models import MainTask, UserProfile, User


class TaskCraetionForm(forms.ModelForm):

    TASK_STATUS_CHOICES = [
    ('ST', 'STARTED'),
    ('NS', 'NOT STARTED'),
    ('IP', 'IN PROGRESS'),
    ('PA', 'PAUSED'),
    ('CO', 'COMPLETED'),
    ]

    
    task_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Task Title'}))
    global_task_info = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Task Description'}))
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'picker'
        }))
    global_task_assign = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control'} ))
    task_status = forms.ChoiceField(label='', choices=TASK_STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = MainTask
        fields = ['task_title',
            'global_task_info',
            'due_date',
            'global_task_assign',
            'task_status',
 
        ]