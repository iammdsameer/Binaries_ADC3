from django.urls import path
from . import views

urlpatterns = [
   path('', views.music, name="music"),
   path('upload/',views.upload,name = "upload_music"),
   
]