from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from account.forms import UserForm
from django.template.context_processors import request
from multiprocessing.sharedctypes import template

def register(request):
    
    template = 'account/register.html'
    if request.method =='GET':
        return render(request, template,{'userForm':UserForm()})
    
    #post
    
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})
    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')
    
def login(request):
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template)
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        messages.error(request, '請填資料')
        return render(request, template)
    
    user = authenticate(username=username, password=password)
    if not user:
        messages.error(request, 'login fail')
        return render (request,template)
    
    auth_login(request, user)
    messages.success(request, 'login success')
    return redirect('main:main')
    
def logout(request):
    
    auth_logout(request)
    messages.success(request, 'welcome again')
    return redirect('main:main')
    
    
# Create your views here.
