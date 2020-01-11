from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Music(models.Model):
    # How to use
     #music_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    music_length = models.FloatField(null=True)
    music_title = models.CharField(max_length=250)
    music_file = models.FileField(default='')
    music_coverArt = models.CharField(max_length=2083, default='https://bit.ly/2FDO3LI')
    #music_coverArt = models.ImageField(upload_to='media/')
    music_file = models.FileField(upload_to='musics/', blank =True)

    def __str__(self):
        return self.music_title
