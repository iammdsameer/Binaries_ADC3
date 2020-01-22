from django import forms
from .models import Musics, Albums,Genres


class UploadMusic(forms.ModelForm):
    class Meta:
        model = Musics
        fields  = (
            'music_length',
            'music_title',
            'music_file',
            'music_genre',
            'music_artist',
            'music_album',
            'music_coverArt',
            
            )
class AddAlbum(forms.ModelForm):
    class Meta:
        model = Albums
        fields = (
            
            'artist',
            'album_title',
            'album_logo',
            
        )

class AddGenre(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ('name','genre_logo',)