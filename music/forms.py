from django import forms
from .models import Musics, Albums, Genres, Distributors, Artists


class UploadMusic(forms.ModelForm):
    class Meta:
        model = Musics
        fields = (
            "music_title",
            "music_length",
            "music_file",
            "music_genre",
            "artist",
            "music_album",
            "music_coverArt",
        )
        # displays 'Select' in option's field

    def __init__(self, *args, **kwargs):
        super(UploadMusic, self).__init__(*args, **kwargs)
        self.fields["music_genre"].empty_label = "Select Genre"
        self.fields["music_album"].empty_label = "Select Album"
        self.fields["artist"].empty_label = "Select Artist"

        # requirement or not
        self.fields["music_length"].required = False


# add musics' belonging albums
class AddAlbum(forms.ModelForm):
    class Meta:
        model = Albums
        fields = (
        
            
            "album_title",
            "year",
            "album_logo",
            "distributor",
        )
    def __init__(self, *args, **kwargs):
        super(AddAlbum, self).__init__(*args, **kwargs)
        self.fields["distributor"].empty_label = "Select Distributor"
        

class AddDistributor(forms.ModelForm):
    class Meta:
        model = Distributors
        fields = '__all__'
class AddArtist(forms.ModelForm):
    class Meta:
        model = Artists
        fields='__all__'

# add musics' genere
class AddGenre(forms.ModelForm):
    class Meta:
        model = Genres
        fields = (
            "name",
            "genre_logo",
        )

