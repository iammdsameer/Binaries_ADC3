from django.shortcuts import render
from .models import Music
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages



def music(request):
    music = Music.objects.all()
    return render(request,'music/music.html',{'music':music})

def upload(request):
    if request.method == 'POST':
        music_title = request.POST['music_title']
        music_artist = request.POST['music_artist']
        music_length = request.POST['music_length']
        music_album = request.POST['music_album']
        music_coverArt = request.POST['music_coverArt']
        music_file = request.POST['music_file']
        upload = Music(music_title=music_title,music_artist=music_artist, music_album=music_album,music_coverArt=music_coverArt, music_file=music_file, music_length=music_length)
        upload.save()
        return HttpResponse('File Uploaded')
    else:   
        return render(request,'music/upload.html')

def deleteMusic(request):
    music=Music.objects.all()
    if request.method =='POST':
       music_id = request.POST['id']
       Music.objects.get(id = music_id).delete()
       messages.success(request,f"You successfully deleted")
    
    return render(request,'music/deleteMusic.html',{'music':music})
def editMusic(request):
    music=Music.objects.all()
    if request.method =='POST':
        music_id =request.POST['id']
        music_artist = request.POST['music_artist']
        music_title = request.POST['music_title']
        music_length = request.POST['music_length']
        music_album = request.POST['music_album']
        music_coverArt = request.POST['music_coverArt']
        music_file = request.POST['music_file']
        Music.objects.filter(id = music_id).update(music_title=music_title,music_artist=music_artist, music_album=music_album,music_coverArt=music_coverArt, music_file=music_file, music_length=music_length)
        
    return render(request,'music/editMusic.html',{'music':music})

def playMusic(request):
    
    pass

def pauseMusic(request):
    pass

def shuffalMusic(request):
    pass

def changeMusic(request):
    #next music
    #prev music
    pass

