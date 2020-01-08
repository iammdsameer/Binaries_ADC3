from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request,'user/request.html',context={})


def login(request):
    return render(request,'user/login.html',context={})


def logout(request):
    pass

def profile(request):
    return render(request,'user/profile.html',context={})

