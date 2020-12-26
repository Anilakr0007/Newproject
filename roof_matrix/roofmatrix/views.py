from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
import psycopg2
from django import template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.

# class Login(View):
#     def index(self,request):
#         return render(request,'index.html')
#
#
#     def loginview(self,request):
#         return render(request,'login.html')
#
#
#     @login_required
#     def dashboardview(self,request):
#         return render(request,'dashboard.html')

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard')
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Correct the errors below')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'register.html', {'form': form})

class RegisterView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Correct the errors below')

def dashboard(request):
    return render(request,'dashboard.html')