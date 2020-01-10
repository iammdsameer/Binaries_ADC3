from django.db import models
import datetime
#from PIL import image


class music(models.Model):
    music_title = models.CharField(max_length=200)
    music_artist = models.CharField(max_length=200)
    music_length = models.CharField(max_length=200)
    music_album = models.CharField(max_length=200)
   # music_coverArt = models.ImageField(upload_to='Cover_Art')
    date_added = datetime.datetime.now()


class contact(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.IntegerField()
    contact_message = models.TextField()


class customer(models.Model):
    f_name = models.CharField(max_length=200)
    m_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
