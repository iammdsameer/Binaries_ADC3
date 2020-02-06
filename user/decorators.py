from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper_func(request, *args,**kwrgs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwrgs)
    
    return wrapper_func
