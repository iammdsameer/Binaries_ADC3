from django.shortcuts import render
from .models import Musics, Albums, Genres
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import UploadMusic, AddAlbum, AddGenre

def index(request):
    music = Musics.objects.all()
    if request.GET:
        query = request.GET['q']
        music = get_data_queryset(str(query))

    return render(request, 'music/index.html', {'musics': music})

# only a logged in user can
def upload(request):
    if request.method == 'POST':
       form = UploadMusic(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           #return redirect('music:homepage')
    form = UploadMusic()
    return render (request,'music/upload.html',{'form':form})

def deleteMusic(request):
    music=Musics.objects.all()
    if request.method =='POST':
       music_id = request.POST['id']
       Musics.objects.get(id = music_id).delete()
       messages.success(request,f"You successfully deleted")
    
    return render(request,'music/deleteMusic.html',{'music':music})


def editMusic(request):
    music=Musics.objects.all()
    if request.method =='POST':
        music_id =request.POST['id']
        music_artist = request.POST['music_artist']
        music_title = request.POST['music_title']
        music_length = request.POST['music_length']
        music_album = request.POST['music_album']
        music_coverArt = request.POST['music_coverArt']
        music_file = request.POST['music_file']
        Musics.objects.filter(id = music_id).update(music_title=music_title,music_artist=music_artist, music_album=music_album,music_coverArt=music_coverArt, music_file=music_file, music_length=music_length)
        
    return render(request,'music/editMusic.html',{'music':music})

def addGenre(request):
    if request.method == 'POST':
       form = AddGenre(request.POST)
       if form.is_valid():
           form.save()
           #return redirect('music:homepage')
    form = AddGenre()
    genres = Genres.objects.all()
    return render (request,'music/addGenre.html',{'form':form,'genre':genres})

def addAlbums(request):
     
     if request.method == 'POST':
       form = AddAlbum(request.POST)
       if form.is_valid():
           form.save()
           return redirect('music:homepage')
     form = AddAlbum()
     albums  =Albums.objects.all()
     return render (request,'music/addAlbum.html',{'form':form,'albums':albums})


def pauseMusic(request):
    pass

def shuffalMusic(request):
    pass

def changeMusic(request):
    #next music
    #prev music
    pass



def get_data_queryset(query=None):
    queryset = []
    queries = query.split(' ')
    for q in queries:
        music = Musics.objects.filter(
            Q(music_title__icontains = q) |
            Q(music_artist__icontains = q) | Q(music_album__icontains = q)
        )

        for m in music:
            queryset.append(m)
    return list(set(queryset))
