from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.sites.models import Site
from django.contrib.admin import ModelAdmin

User = get_user_model()



# @admin.register(Site)
# class UserSiteAdmin(ModelAdmin):
#     fields = ('id','name','domain')
#     readonly_fields = ('id')
#     list_display = ('id','name','domain')
#     list_display_links = ('name',)
#     search_fields = ('name','domain')


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password',),
        }),
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('first_name','middle_name','last_name','gender','email'),
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active','is_staff','is_superuser','user_permissions',),
        }),
        ('Important dates', {
            'classes': ('wide',),
            'fields': ('last_login','date_joined',),
        }),
        ('More Details', {
            'classes': ('wide',),
            'fields': ('profession','course',),
        }),
    )
    list_display = ('username','email', 'first_name','middle_name', 'last_name','gender','profession','course','is_staff')
    search_fields = ('username','email','first_name')
    list_filter = ('gender','course')

admin.site.site_header = "Ed-Flix Administration"
admin.site.site_title = "Ed-Flix Admin Portal"
admin.site.index_title = "Welcome to Ed-Flix Admin Portal"

admin.site.register(User,UserAdmin)