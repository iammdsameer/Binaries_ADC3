from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, 'musicLib/index.html', context={})


def register(request):
    return HttpResponse("this is where we register")


def login(request):
    pass


def logout(request):
    pass


def profile(request):
    pass
