from django.shortcuts import render
from music.models import Music
from django.http import HttpResponse



def index(request):
   
    if request.method == "POST":
        search_tag = request.POST['search_tag']
        result = Music.objects.filter(music_title__contains=search_tag)
        print(result)
        return render(request, 'musicLib/index.html', context={'result':result})
    else:
        data = "Sorry !! No Data Found"
        return render(request,'musicLib/index.html',{'data':data})
    


