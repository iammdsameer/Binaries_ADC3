from django.shortcuts import render, redirect
from music.models import Musics
from .models import Customers
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated
from .forms import registerform, customerform


# user register if already logged in redirects to  home page
@unauthenticated
def register(request):
    if request.method == 'POST':
        uform = registerform(request.POST)
        cform = customerform(request.POST)
        try:
            # checks for any user existance with same username
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'user/register.html', {'error': 'Error: Username is already taken', 'form': uform, 'cform': cform})
        except User.DoesNotExist:
            # checks for form validation
            if uform.is_valid() and cform.is_valid():
                user = uform.save()
                # holds with data before another save is called
                customer = cform.save(commit=False)
                customer.user = user
                customer.save()
                # gets data from the form
                username = uform.cleaned_data.get('username')
                password = uform.cleaned_data.get('password')
                # authentication
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("/user/profile/")

    else:
        # django user
        uform = registerform()
        # customer model user
        cform = customerform()
    context = {'form': uform, 'cform': cform}
    return render(request, "user/register.html", context)

# user login if already logged in redirects to  home page
@unauthenticated
def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "user/login.html", {"error": "You got your password or username wronged!!!"})
    else:

        return render(request, "user/login.html")


# log out function -->> redirects to index
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("music:homepage")

# user profile


@login_required(login_url='/user/login/')
def profile(request):
    music = Musics.objects.all()
    if request.user.is_superuser == False:
        user = request.user.id
        customer = Customers.objects.get(user=user)
        premium = customer.is_premium
        return render(request, "user/profile.html", context={"musics": music, 'premium': premium})
    else:
        return render(request, "user/profile.html", context={"musics": music, 'premium': True})
