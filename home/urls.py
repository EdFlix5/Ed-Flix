from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.index,name="home"),
    
    #apis
    path('api/login',views.log_in,name="login"),
    path('api/signup',views.signup,name="signup"),
    path('api/logout',views.signout,name="signout"),
]
