from django.shortcuts import render
from music.models import Musics
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def data(request):
     if request.method == "GET":
        music = Musics.objects.all() 
        dict_type = {"musics": list(music.values("music_title", "music_length"))}
        return JsonResponse(dict_type)

def get_music(request,pk):
    if request.method=='GET':
        try:
            music = Musics.objects.get(pk=pk)
            result_data = json.dumps([{'Title':music.music_title,'Length':music.music_length}])
            return HttpResponse(result_data, content_type='text/json')
        except:
            return JsonResponse({"Error":f"No such data found with id:{pk}"})
        
@csrf_exempt   
def edit(request, pk):
    music = Musics.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"musics": music.music_title, "length": music.music_length})

    elif request.method =="PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        music.music_title = update_data['music_title']
        music.music_length = update_data['music_length']
        music.save()
        return JsonResponse({'Success': 'Upadated Successfully!!'})
    elif request.method =="DELETE":
        music.delete()
        return JsonResponse({'Success': 'Music Deleted'})
        
@csrf_exempt    
def addMusic(request):
    if request.method =='POST':
        json_data = request.body.decode('utf-8')
        new = json.loads(json_data)
        music_title = new['title']
        length = new['length']
        music = Musics.objects.create(music_title=music_title,music_length=length)
        try:
            music.save()
            return JsonResponse({"Success":"New music added successfully!!"})
        except:
            return JsonResponse({"Error":"Music could not be added"})
        
        
        
def music_pagination(request,PAGENO,SIZE):
    skip = SIZE*(PAGENO-1)
    music = Musics.objects.all()[skip:(PAGENO*SIZE)]
    dict = {
        "musics":list(music.values("music_title","artist","music_length"))
    }
    return JsonResponse(dict)