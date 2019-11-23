import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager



# Create your models here.
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, unique=False)
    family_name = models.CharField(max_length=50, unique=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/', default='images/def_user.png')
    teams_link = models.URLField(blank = True, max_length=200)
    mobile_phone = models.CharField(max_length=16, blank=True)
    user_location = models.CharField(max_length=80, blank=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True



class MainTask(models.Model):
    task_title = models.CharField(max_length=200)
    global_task_info = models.TextField(max_length=500,default=None) 
    complete = models.BooleanField(default=False)
    overall_precent_complete = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    due_date = models.DateTimeField(default=datetime.datetime.now())

    global_task_assign = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="global_task_assign",default=1)
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


    task_assign = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="task_assign",default=1)
    

    def __str__(self):
        return self.task_description




            