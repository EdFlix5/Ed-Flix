from django.contrib import admin
from .models import User
from .forms import EdFlixUserAuthenticationForm,EdFlixUserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    #add_form = EdFlixUserCreationForm
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','middle_name', 'last_name','gender','profession','course',),
        }),
    )
    list_display = BaseUserAdmin.list_display + ('gender','profession','course',)
    

admin.site.site_header = "Ed-Flix Administration"
admin.site.site_title = "Ed-Flix Admin Portal"
admin.site.index_title = "Welcome to Ed-Flix Admin Portal"

admin.site.register(User,UserAdmin)