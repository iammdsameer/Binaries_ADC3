from django.shortcuts import render, redirect
from .models import Musics, Albums, Genres, Artists, Distributors

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import UploadMusic, AddAlbum, AddGenre, AddArtist, AddDistributor
from django.contrib.auth.decorators import login_required
from .decorators import admin
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.decorators import authenticated

# Returns index page with list of added songs
@authenticated
def index(request):
    music = Musics.objects.all()
    if request.GET:
        query = request.GET["q"]
        music = get_data_queryset(str(query))

    return render(request, "music/index.html", {"musics": music})


# Upload Music only by logged in users

@login_required(login_url="/user/login/")
@admin
def upload(request, pk=0):
    if request.method == "GET":
        if pk == 0:
            form = UploadMusic()
        else:
            music = Musics.objects.get(pk=pk)
            form = UploadMusic(instance=music)
        return render(request, "music/upload.html", {"form": form})
    else:

        form = UploadMusic(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/upload/")


# delete added music authenticated users only
@login_required(login_url="/user/login/")
@admin
def deleteMusic(request, pk):

    music = Musics.objects.get(pk=pk)
    music.delete()
    return redirect("/user/profile/")


@login_required(login_url="/user/login/")
@admin
def addGenre(request):
    if request.method == "POST":
        form = AddGenre(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('music:homepage')
    form = AddGenre()
    genres = Genres.objects.all()
    return render(request, "music/addGenre.html", {"form": form, "genre": genres})


# add music albums
@login_required(login_url="/user/login/")
@admin

def addAlbums(request): 

    if request.method == "POST":
        form = AddAlbum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addAlbum/')
    form = AddAlbum()
    albums = Albums.objects.all()
    return render(request, "music/addAlbum.html", {"form": form, "albums": albums})

#addDistributor only logged in administrator  can
@login_required(login_url="/user/login/")
@admin

def addDistributor(request):

    if request.method == "POST":
        form = AddDistributor(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('music:homepage')
    form = AddDistributor()
    dis = Distributors.objects.all()
    return render(request, "music/addDistributor.html", {"form": form, "dis": dis})

#addArtist only logged in administrator  can
@login_required(login_url="/user/login/")
@admin
def addArtist(request):

    if request.method == "POST":
        form = AddArtist(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addArtist/')
    form = AddArtist()
    artist = Artists.objects.all()
    return render(request, "music/addArtist.html", {"form": form, "artist": artist})


# search  functionality
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(
        " "
    )  # splits after every white space for searching each keyword
    for q in queries:
        music = Musics.objects.filter(Q(music_title__icontains=q) | Q(music_album__album_title__icontains=q) | Q(artist__name__icontains=q))

        for m in music:
            queryset.append(m)
    return list(set(queryset))  # queries type casted to list
