from django.shortcuts import render,redirect
from django.http import HttpResponse
import psycopg2
from django import template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.

class Login(View):
    def index(self,request):
        return render(request,'index.html')


    def loginview(self,request):
        return render(request,'login.html')


    @login_required
    def dashboardview(self,request):
        return render(request,'dashboard.html')

    def registerview(self,request):
        if request.method=='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm
        return render(request,'register.html',{'form':form})
