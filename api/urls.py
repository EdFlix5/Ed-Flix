from django.conf.urls import url
from django.urls import path,include

from . import views

urlpatterns = [
    path('login',views.login,name="api_login"),
    path('signup',views.signup,name="api_signup"),
    path('logout',views.signout,name="api_logout"),
    path('upload',views.upload_file,name="api_upload"),
    path('docs',views.allDocs,name="api_docs"),
    path('visit',views.allVisit,name="api_visit"),
    path('advancedSearch',views.advancedSearch,name="api_advanced_search"),
    path("clear",views.clear,name="api_clear"),
]
