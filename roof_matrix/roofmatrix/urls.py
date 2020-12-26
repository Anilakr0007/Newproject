from django.http import HttpResponse
from django.urls import include,path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #path('',views.Login.as_view(),name='index'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    ]