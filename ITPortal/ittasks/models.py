import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class MainTask(models.Model):
    task_title = models.CharField(max_length=200)
    global_task_info = models.TextField(max_length=500,default=None) 
    complete = models.BooleanField(default=False)
    overall_precent_complete = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    due_date = models.DateTimeField(default=datetime.datetime.now())

    global_task_assign = models.ForeignKey(User, on_delete=models.CASCADE, related_name="global_task_assign",default=1)
    TASK_STATUS_CHOICES = [
    ('ST', 'STARTED'),
    ('NS', 'NOT STARTED'),
    ('IP', 'IN PROGRESS'),
    ('PA', 'PAUSED'),
    ('CO', 'COMPLETED'),
]
    task_status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default='NOT STARTED')

    def __str__(self):
        return self.task_title



class ChildTask(models.Model):
    # Relationship Fields
    item_main = models.ForeignKey('MainTask',on_delete=models.CASCADE, related_name="item_main", )
    task_description = models.CharField(max_length=200)
    task_info = models.TextField(blank = True)
    task_complete = models.BooleanField(default=False)
    sub_task = models.CharField(max_length=200)
    task_precent_complete = models.PositiveIntegerField(default=0)
    task_created = models.DateTimeField(default=datetime.datetime.now())
    task_updated_at = models.DateTimeField(default=datetime.datetime.now())
    task_due_date = models.DateTimeField(default=datetime.datetime.now())


    task_assign = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_assign",default=1)
    

    def __str__(self):
        return self.task_description



class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/')
    mobile_number = 
    teams_link = models.URLField(blank = True, max_length=200)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
            