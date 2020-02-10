from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Customers
from .decorators import alreadyPremium
from user.decorators import authenticated


@alreadyPremium
@authenticated
def payment(request):
    if request.method == "GET":
        return render(request, "payment/payment.html", context={})
    else:
        cname = request.POST["cname"]
        cvv = request.POST["cvv"]
        user = request.user.id
        customer = Customers.objects.get(user=user)
        pk = customer.id
        if cname == "binaries" and cvv == '1212':
            Customers.objects.filter(pk=pk).update(is_premium=True)

            return redirect('/user/profile/')
        else:
            return HttpResponse("Payment Unsuccessfull!!!")
