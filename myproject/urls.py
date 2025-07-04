"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.views import CustomPasswordResetView
urlpatterns = [
    path('admin/',admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('land/',views.landingread,name='landing'),
    path('loginread',views.loginread,name='login'),
    path('login/', views.user_login, name='login'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('privacyread',views.privacyread,name='privacy'),
    path('profileread',views.profileread,name='profile'),
    path('courseread',views.courseread,name='course'),
    path('profilecreate',views.profilecreate,name='profilecreate'),
    path('enrolled',views.enrolled,name='enroll'),




]

