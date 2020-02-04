from django.shortcuts import render, redirect
from .models import Musics, Albums, Genres
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import UploadMusic, AddAlbum, AddGenre
from django.contrib.auth.decorators import login_required

# Returns index page with list of added songs
def index(request):
    music = Musics.objects.all()
    if request.GET:
        query = request.GET["q"]
        music = get_data_queryset(str(query))

    return render(request, "music/index.html", {"musics": music})


# Upload Music only by logged in users
@login_required(login_url="/user/login/")
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
            return redirect("/")


# delete added music authenticated users only
@login_required(login_url="/user/login/")
def deleteMusic(request, pk):

    music = Musics.objects.get(pk=pk)
    music.delete()
    return redirect("/user/profile/")


# Update MusicInfo
# def editMusic(request, pk):
#     music = Musics.objects.all()
#     form = UploadMusic()

#     if request.method == "POST":
#         music = Musics.objects.get(pk=pk)
#         form = UploadMusic(instance=music)
#         music_id = request.POST["id"]
#         music_artist = request.POST["music_artist"]
#         music_title = request.POST["music_title"]
#         music_length = request.POST["music_length"]
#         music_album = request.POST["music_album"]
#         music_coverArt = request.POST["music_coverArt"]
#         music_file = request.POST["music_file"]
#         Musics.objects.get(pk=pk).update(
#             music_title=music_title,
#             music_artist=music_artist,
#             music_album__album_title=music_album,
#             music_coverArt=music_coverArt,
#             music_file=music_file,
#             music_length=music_length,
#         )

#     return render(request, "music/editMusic.html", {"music": music})


# add music genere
@login_required(login_url="/user/login/")
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
        music = Musics.objects.filter(Q(music_title__icontains=q) | Q(music_album__album_title__icontains=q) | Q(music_artist__icontains=q))

        for m in music:
            queryset.append(m)
    return list(set(queryset))  # queries type casted to list
