from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect




def index(request):
    costumers = Customers.objects.all()
    if request.GET:
        query = request.GET['q']
        costumers = get_data_queryset(str(query))

    return render(request, 'user/login.html', {'user': user})

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


def user_login(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
    else:
        context['error'] = "Provide valid credentials !!"
        return render(request, 'user/login.html',context)


def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    context = {}
    context['user'] = request.user
    return render(request,'user/profile.html',context={})

def contact(request):
    #if request.method=="POST":
        #name=request.POST['name']

       return render(request,'user/contact.html',context={})  

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(' ')
    for q in queries:
        costumers = Costumers.objects.filter(
            Q(f_name__icontains=q) |
            Q(l_name__icontains=q) | Q(email__icontains=q)
        )

        for c in costumers:
            queryset.append(c)
    return list(set(queryset))
