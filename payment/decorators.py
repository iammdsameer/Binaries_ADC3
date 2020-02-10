from django.http import HttpResponse
from django.shortcuts import redirect
from user.models import Customers


def alreadyPremium(view_func):
    def wrapper_func(request, *args, **kwrgs):
        # if user is already premium user; redirect to profile page
        user = request.user.id
        customer = Customers.objects.get(user=user)
        premium = customer.is_premium

        if premium:
            return redirect('/user/profile/')
        else:
            return view_func(request, *args, **kwrgs)

    return wrapper_func
