from django.shortcuts import render, redirect
from music.models import Musics
from .models import Customers
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required




def register(request):
    
    if request.method =='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'user/register.html',{'error':'Error: Username is already taken'})
            except User.DoesNotExist:
                f_name = request.POST['first_name'].capitalize()
                l_name = request.POST['last_name'].capitalize()
                m_name = request.POST['middle_name'].capitalize()
                dob = request.POST['dob']
                phone = request.POST['phone']
                country = request.POST['country']
                gender = request.POST['gender']
                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                user = User.objects.create_user(username=username, password=password1)
                
                customers = Customers(email=email,f_name=f_name,l_name=l_name,m_name=m_name,dob=dob,phone=phone,gender = gender, country=country)
                
                auth.login(request,user)
                return redirect('user:profile')
        else:
             return render(request, "user/register.html", context={'error':'Error: Password Do not match'})

    else:
        return render(request, "user/register.html", context={})

def edit(request,pk):
    if request.method =='POST':
        f_name = request.POST['first_name'].capitalize()
        l_name = request.POST['last_name'].capitalize()
        m_name = request.POST['middle_name'].capitalize()
        dob = request.POST['dob']
        phone = request.POST['phone']
        country = request.POST['country']
        gender = request.POST['gender']
        customers = Customers.objects.filter(pk=pk).update(email=email,f_name=f_name,l_name=l_name,m_name=m_name,dob=dob,phone=phone,gender = gender, country=country)
                

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("user:profile")
    else:
        context["error"] = "Provide valid credentials !!"
        return render(request, "user/login.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("music:homepage")

@login_required(login_url='/user/login/')
def profile(request):
    music = Musics.objects.all()
    # context['user'] = request.user
    if request.POST:

        customer_id = request.POST["cid"]
        Customers.objects.filter(id=cid).update(is_premium="True")

    return render(request, "user/profile.html", context={"musics": music})

def contact(request):
    # if request.method=="POST":
    # name=request.POST['name']

    return render(request, "user/contact.html", context={})


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        costumers = Costumers.objects.filter(
            Q(f_name__icontains=q) | Q(l_name__icontains=q) | Q(email__icontains=q)
        )

        for c in costumers:
            queryset.append(c)
    return list(set(queryset))
