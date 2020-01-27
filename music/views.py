from django.shortcuts import render, redirect
from .models import Musics, Albums, Genres
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import UploadMusic, AddAlbum, AddGenre

# Returns index page with list of added songs
def index(request):
    music = Musics.objects.all()
    if request.GET:
        query = request.GET["q"]
        music = get_data_queryset(str(query))

    return render(request, "music/index.html", {"musics": music})


# Upload Music only by logge in users
def upload(request, pk=0):
    if request.method == "GET":
        if pk == 0:
            form = UploadMusic()
        else:
            music = Musics.objects.get(pk=pk)
            form = UploadMusic(instance=music)
        return render(request, "music/upload.html", {"form": form})
    else:
        if pk == 0:
            form = UploadMusic(request.POST)
        else:

            form = UploadMusic(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect("/")


# delete added music authenticated users only
def deleteMusic(request, pk):

    music = Musics.objects.get(pk=pk)
    music.delete()
    return redirect("/user/profile/")


# Update MusicInfo
def editMusic(request):
    music = Musics.objects.all()
    if request.method == "POST":
        music_id = request.POST["id"]
        music_artist = request.POST["music_artist"]
        music_title = request.POST["music_title"]
        music_length = request.POST["music_length"]
        music_album = request.POST["music_album"]
        music_coverArt = request.POST["music_coverArt"]
        music_file = request.POST["music_file"]
        Musics.objects.filter(id=music_id).update(
            music_title=music_title,
            music_artist=music_artist,
            music_album=music_album,
            music_coverArt=music_coverArt,
            music_file=music_file,
            music_length=music_length,
        )

    return render(request, "music/editMusic.html", {"music": music})


# add music genere
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
def addAlbums(request):

    if request.method == "POST":
        form = AddAlbum(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('music:homepage')
    form = AddAlbum()
    albums = Albums.objects.all()
    return render(request, "music/addAlbum.html", {"form": form, "albums": albums})


# search  functionality
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(
        " "
    )  # splits after every white space for searching each keyword
    for q in queries:
        music = Musics.objects.filter(
            Q(music_title__icontains=q)
            | Q(music_artist__icontains=q)
            | Q(music_album__icontains=q)
        )

        for m in music:
            queryset.append(m)
    return list(set(queryset))  # queries type casted to list
