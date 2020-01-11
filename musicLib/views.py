from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        search_tag = request.POST['search_tag']
      
    return render(request, 'musicLib/index.html', context={})


