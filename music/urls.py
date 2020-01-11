from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "music"

urlpatterns = [
   path('', views.music, name="music"),
   path('upload/',views.upload,name = "upload_music"),
   path('del/',views.deleteMusic,name = 'manage'),
   path('edit/',views.editMusic,name = 'manage'),
]
