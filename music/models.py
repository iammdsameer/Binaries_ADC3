from django.db import models

# Create your models here.
class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Musics(models.Model):
    # How to use
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    music_length = models.IntegerField(null = True)
    music_title = models.CharField(max_length=250)
    music_file = models.FileField(default='')
    music_artist = models.CharField(max_length=250, null = True)
    music_album = models.CharField(max_length=250, null=True)
    
    music_coverArt = models.CharField(max_length=2083, default="https://i.ytimg.com/vi/5Peo-ivmupE/maxresdefault.jpg")

    def __str__(self):
        return self.music_title

    def double_check_values(self):
        return True
