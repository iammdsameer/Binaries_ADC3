from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "music"

urlpatterns = [
<<<<<<< HEAD
   path('', views.index, name="homepage"),
   path('upload/', views.upload, name = "upload_music"),
   path('del/',views.deleteMusic,name = 'manage'),
   path('edit/',views.editMusic,name = 'manage'),
   path('addGenre/',views.addGenre,name = 'addGenre'),
   path('addAlbum/',views.addAlbums,name = 'addAlbum'),
   
=======
    path("", views.index, name="homepage"),
    path("upload/", views.upload, name="upload_music"),
    path("delete/<int:pk>", views.deleteMusic, name="delete"),
    path("<int:pk>/", views.upload, name="edit"),
    path("addGenre/", views.addGenre, name="addGenre"),
    path("addAlbum/", views.addAlbums, name="addAlbum"),
>>>>>>> 4da5b6d7f9b8ba943c0bc3aaa3fd63388b3ffaf6
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
