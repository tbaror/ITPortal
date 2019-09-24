from django.contrib import admin
from .models import MainTask ,ChildTask

# Register your models here.
admin.site.register(MainTask )
admin.site.register(ChildTask)