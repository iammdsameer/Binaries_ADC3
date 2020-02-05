from django.db import models

# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=250, default= "Unknown")
    image = models.CharField(max_length = 2083, default = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fclipart-library.com%2Fimg%2F870190.png&f=1&nofb=1")
    def __str__(self):
        return self.name
class Distributors(models.Model):
    name = models.CharField(max_length=250, default= "Unknown")
    logo = models.CharField(max_length=2083, default = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmdbootstrap.com%2Fimg%2FPhotos%2FOthers%2Fplaceholder-avatar.jpg&f=1&nofb=1")
    def __str__(self):
        return self.name
class Albums(models.Model):
    distributor = models.ForeignKey(Distributors,on_delete=models.CASCADE, null = True)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(default=2020)
    album_logo = models.CharField(
        max_length=2083, default="https://i.ytimg.com/vi/5Peo-ivmupE/maxresdefault.jpg"
    )

    def __str__(self):
        return self.album_title


class Genres(models.Model):
    name = models.CharField(max_length=200)
    genre_logo = models.CharField(
        max_length=2083, default="https://i.ytimg.com/vi/5Peo-ivmupE/maxresdefault.jpg"
    )

    def __str__(self):
        return self.name


class Musics(models.Model):
    
    artist = models.ForeignKey(Artists,on_delete=models.CASCADE, null=True)
    music_length = models.IntegerField(null=True)
    music_title = models.CharField(max_length=250)
    music_file = models.FileField(upload_to="media/")
    music_genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    
    music_album = models.ForeignKey(Albums, on_delete=models.CASCADE, null=True)
    music_coverArt = models.CharField(
        max_length=2083, default="https://i.ytimg.com/vi/5Peo-ivmupE/maxresdefault.jpg"
    )

    def __str__(self):
        return self.music_title

    def double_check_values(self):
        return True
