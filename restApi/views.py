from django.shortcuts import render
from music.models import Musics
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def data(request):
     if request.method == "GET":
        music = Musics.objects.all() 
        dict_type = {"musics": list(music.values("music_title", "music_length"))}
        return JsonResponse(dict_type)
@csrf_exempt   
def edit(request, pk):
    music = Musics.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"musics": music.music_title, "length": music.music_length})

    else:
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        music.music_title = update_data['title']
        music.music_length = update_data['length']
        music.save()
        return JsonResponse({'message': 'Upadated Successfully!!'})
    

def music_pagination(request,PAGENO,SIZE):
    skip = SIZE*(PAGENO-1)
    music = Musics.objects.all()[skip:(PAGENO*SIZE)]
    dict = {
        "musics":List(Musics.values("music_title","artist","music_length"))
    }
    return JsonResponse(dict)