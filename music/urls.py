from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "music"

urlpatterns = [
   path('', views.index, name="homepage"),
   path('upload/',views.upload,name = "upload_music"),
   path('del/',views.deleteMusic,name = 'manage'),
   path('edit/',views.editMusic,name = 'manage'),
   path('addGenre/',views.addGenre,name = 'addGenre'),
   path('addAlbum/',views.addAlbums,name = 'addAlbum'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)