from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import MainTask, UserProfile, User, ChildTask
from django.urls import reverse
from django.forms import inlineformset_factory



class TaskCraetionForm(forms.ModelForm):

    TASK_STATUS_CHOICES = [
    ('ST', 'STARTED'),
    ('NS', 'NOT STARTED'),
    ('IP', 'IN PROGRESS'),
    ('PA', 'PAUSED'),
    ('CO', 'COMPLETED'),
    ]
    INPUTֹTIMEֹFORMATS = ['%Y-%m-%d',      # '2006-10-25'
'%m/%d/%Y',
'%Y/%m/%d',       # '10/25/2006'
'%Y/%m/%d %H:%M',
'%m/%d/%y',
'%Y-%m-%d %H:%M:%S']       # '10/25/06'
    
    task_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Task Title'}))
    global_task_info = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Task Description'}))
    due_date = forms.DateTimeField(input_formats=INPUTֹTIMEֹFORMATS, widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'picker'
        }))
    global_task_assign = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control'} ))
    task_status = forms.ChoiceField(label='', choices=TASK_STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    task_location = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Task Location'}))

    class Meta:
        model = MainTask
        fields = ['task_title',
            'global_task_info',
            'due_date',
            'global_task_assign',
            'task_status',
            'task_location',
 
        ]

        


class TaskUpdateForm(ModelForm):

    TASK_STATUS_CHOICES = [
        ('ST', 'STARTED'),
        ('NS', 'NOT STARTED'),
        ('IP', 'IN PROGRESS'),
        ('PA', 'PAUSED'),
        ('CO', 'COMPLETED'),
        ]
    INPUTֹTIMEֹFORMATS = ['%Y-%m-%d',      # '2006-10-25'
        '%m/%d/%Y',
        '%Y/%m/%d',       # '10/25/2006'
        '%Y/%m/%d %H:%M',
        '%m/%d/%y',
        '%Y-%m-%d %H:%M:%S']       # '10/25/06'

    #Main Task objects
    task_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Task Title'}))
    global_task_info = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Task Description'}))
    due_date = forms.DateTimeField(required=False, input_formats=INPUTֹTIMEֹFORMATS, widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'picker'
        }))
    global_task_assign = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control'} ))
    task_status = forms.ChoiceField(label='', choices=TASK_STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    complete = forms.BooleanField( required=False, widget=forms.CheckboxInput(attrs={'type':'checkbox', 'class':'custom-control-input', 'id':'switchcomplete'}))
    overall_precent_complete = forms.IntegerField(widget=(forms.NumberInput(attrs={'type':'range', 'min':'0', 'max':'100', 'value':'50', 'class':'range-slider__range', 'id':'PreRange'})))
    task_location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    
    class  Meta:

        model = MainTask
        fields = ['task_title',
            'global_task_info',
            'due_date',
            'global_task_assign',
            'task_status',
            'complete',
            'overall_precent_complete',
            'task_location',
            'global_task_assign',
            'task_status',]

       



""" class TaskUpdateForm(ModelForm):

    TASK_STATUS_CHOICES = [
        ('ST', 'STARTED'),
        ('NS', 'NOT STARTED'),
        ('IP', 'IN PROGRESS'),
        ('PA', 'PAUSED'),
        ('CO', 'COMPLETED'),
        ]
    INPUTֹTIMEֹFORMATS = ['%Y-%m-%d',      # '2006-10-25'
        '%m/%d/%Y',
        '%Y/%m/%d',       # '10/25/2006'
        '%Y/%m/%d %H:%M',
        '%m/%d/%y',
        '%Y-%m-%d %H:%M:%S']       # '10/25/06'

    #Main Task objects
    task_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Task Title'}))
    global_task_info = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Task Description'}))
    due_date = forms.DateTimeField(required=False, input_formats=INPUTֹTIMEֹFORMATS, widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'picker'
        }))
    global_task_assign = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control'} ))
    task_status = forms.ChoiceField(label='', choices=TASK_STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    complete = forms.BooleanField( required=False, widget=forms.CheckboxInput(attrs={'type':'checkbox', 'class':'custom-control-input', 'id':'switchcomplete'}))
    overall_precent_complete = forms.IntegerField(widget=(forms.NumberInput(attrs={'type':'range', 'min':'0', 'max':'100', 'value':'50', 'class':'range-slider__range', 'id':'PreRange'})))
    task_location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    #Child Tasks objects
    task_description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sub Task Description'}))
    task_info = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Sub Task Description'}))
    task_complete = forms.BooleanField( required=False, widget=forms.CheckboxInput(attrs={'type':'checkbox', 'class':'custom-control-input', 'id':'switchcomplete'}))
    sub_task = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Sub Task Description'}))
    task_precent_complete = forms.IntegerField(widget=(forms.NumberInput(attrs={'type':'range', 'min':'1', 'max':'100', 'value':'50', 'class':'slider', 'id':'myRange'})))
    task_due_date = forms.DateTimeField(input_formats=INPUTֹTIMEֹFORMATS, widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'picker'
        }))
    task_assign = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control'} ))    
      
    class  Meta:

        model = MainTask
        fields = ['task_title',
            'global_task_info',
            'due_date',
            'global_task_assign',
            'task_status',
            'complete',
            'overall_precent_complete',
            'task_location',
            'global_task_assign',
            'task_status',]

        taskidformset = inlineformset_factory(MainTask,ChildTask, fields=('task_description','task_info','task_complete',
    'sub_task','task_precent_complete','task_due_date','task_assign')) """