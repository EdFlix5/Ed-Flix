from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('login',views.log_in,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.signout,name="signout"),
]
