from django.db import models
import datetime
from PIL import image

def music(models.Model):
    music_title = models.CharField(max_length=200)
    music_artist= models.CharField(max_length=200)
    music_length = models.CharField(max_length=200)
    music_album= models.CharField(max_length=200)
    music_coverArt= models.ImageField(upload_to='Cover_Art')
    date_added= datetime.datetime.now()

def contact(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.IntegerField()
    contact_message = models.TextField()

def customer(models.Models):
    f_name
    m_name
    l_name
    dob
    phone
    email
    gender
    
    
    