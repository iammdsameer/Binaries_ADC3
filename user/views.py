from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/')
    else:
        return render(request,'user/register.html',context={})


def login(request):
    return render(request,'user/login.html',context={})


def logout(request):
    pass

def profile(request):
    return render(request,'user/profile.html',context={})

