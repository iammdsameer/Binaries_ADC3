from django import forms
from .models import Musics, Albums,Genres


class UploadMusic(forms.ModelForm):
    class Meta:
        model = Musics
        fields  = (
           
            'music_title',
            'music_length',
            'music_file',
            'music_genre',
            'music_artist',
            'music_album',
            'music_coverArt',
            
            )
        #add musics' belonging albums
class AddAlbum(forms.ModelForm):
    class Meta:
        model = Albums
        fields = (
            
            'artist',
            'album_title',
            'album_logo',
            
        )
#add musics' genere 
class AddGenre(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ('name','genre_logo',)