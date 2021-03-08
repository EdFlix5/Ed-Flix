from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('explore',views.explore,name="explore"),
    path("subjectContent",views.sub_details,name="subjectContent"),
     path("subjectContent/contentView",views.pdf_viewer,name="contentView"),
]
