from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    # path('login',views.user_login,name="login"),
    # path('logout',views.user_logout,name="logout"),
    # path('signup',views.signup,name="signup"),
    #path('password_reset',allauth.account.views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'),name="password_reset"),
    # path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
