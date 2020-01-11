from django.shortcuts import render
from .models import Music
from django.http import HttpResponse



def music(request):
    musics = Music.objects.all()
    return render(request,'music/music.html',{'music':musics})

def upload(request):
    if request.method == 'POST':
        music_title = request.POST['music_title']
        music_length = request.POST['music_length']
        #music_album = request.POST['music_album']
        music_coverArt = request.POST['music_coverArt']
        music_file = request.POST['music_file']
        upload = Music(music_title=music_title, music_coverArt=music_coverArt, music_file=music_file, music_length=music_length)
        upload.save()
        return HttpResponse('File Uploaded')
    else:   
        return render(request,'music/upload.html')

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

