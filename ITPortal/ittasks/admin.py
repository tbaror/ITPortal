from django.contrib import admin
from .models import MainTask ,ChildTask
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ittasks.models import UserProfile

# Register your models here.
admin.site.register(MainTask )
admin.site.register(ChildTask)




class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff','mobile_phone','teams_link','profile_image','user_location','first_name','family_name')
	search_fields = ('email','username','profile_image','teams_link','mobile_phone','user_location','first_name','family_name')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(UserProfile, AccountAdmin)

