from importlib import import_module
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from allauth.socialaccount import providers

from allauth import app_settings


urlpatterns = [
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('signup',views.signup,name="signup"),
    path('password_reset',auth_views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'),name="password_reset"),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]


if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
