from django.http import HttpResponse
from django.urls import include,path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from .views import Login

urlpatterns = [
    path('',views.Login.as_view(),name='index'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('dashboard/',views.Login.as_view(),name='dashboard'),
    path('register/',views.Login.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    ]