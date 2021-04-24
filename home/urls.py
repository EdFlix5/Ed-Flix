from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('explore',views.explore,name="explore"),
    path('docs',views.allDocs,name="docs"),
    path('upload',views.upload,name="upload"),
    path('upload-file',views.upload_file,name="upload_file"),
    path("subjectContent",views.sub_details,name="subjectContent"),
    path("subjectContent/contentView",views.contentView,name="contentView"),
]
