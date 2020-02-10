from django.http import HttpResponse
from django.shortcuts import redirect
from . models import Customers


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwrgs):
        # if user is authenticated can perform operations
        if request.user.is_authenticated:
            return redirect('/user/login/')
        else:
            return view_func(request, *args, **kwrgs)

    return wrapper_func

#when user is authenticated
def authenticated(view_func):
    def wrapper_func(request, *args, **kwrgs):
        # if user is authenticated can perform operations
        if request.user.is_authenticated:
            return view_func(request, *args, **kwrgs)
            
        else:
            return redirect('/user/login/')

    return wrapper_func
