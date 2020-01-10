from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.music, name="music"),
   
]