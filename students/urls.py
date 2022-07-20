from django.urls import path, include
from .views import joinV
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

app_name = 'students'
urlpatterns = [
    path("", joinV, name='join'),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/",LogoutView.as_view(),name='logout'),
    path("changepassword/",PasswordChangeView.as_view(),name='change'),
    path("password_change_done/",PasswordChangeDoneView.as_view(),name='chdone'),
    path("reset/",PasswordResetView.as_view(),name='reset'),
    path("reset_conf/",PasswordResetConfirmView.as_view(),name='resetconf'),
]
