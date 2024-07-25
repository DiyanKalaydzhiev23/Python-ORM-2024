from django import forms

from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.models import Album, Song
from MusicApp.settings import session


class AlbumBaseForm(forms.Form):
    album_name = forms.CharField(
        label="Album Name:",
        max_length=30,
        required=True,
    )

    image_url = forms.URLField(
        label="Image URL:",
        required=True,
    )

    price = forms.DecimalField(
        label="Price:",
        required=True,
        min_value=0.0,
    )


class AlbumCreateForm(AlbumBaseForm):

    @session_decorator(session)
    def save(self):
        new_album = Album(
            album_name=self.cleaned_data['album_name'],
            image_url=self.cleaned_data['image_url'],
            price=self.cleaned_data['price'],
        )

        session.add(new_album)


class AlbumEditForm(AlbumBaseForm):
    def save(self, album):
        album.album_name = self.cleaned_data['album_name']
        album.image_url = self.cleaned_data['image_url']
        album.price = self.cleaned_data['price']


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


class SongBaseForm(forms.Form):
    song_name = forms.CharField(
        label="Song Name:",
        max_length=10,
        required=True
    )

    album = forms.ChoiceField(
        label="Album:",
        choices=[],  # we overwrite that in the init
    )

    music_file_data = forms.FileField(
        label="Music File:",
        required=True,
    )

    @session_decorator(session)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        albums = session.query(Album).all()
        self.fields["album"].choices = [(album.id, album.album_name) for album in albums]


class SongCreateForm(SongBaseForm):

    @session_decorator(session)
    def save(self, request):
        new_song = Song(
            song_name=self.cleaned_data['song_name'],
            album_id=self.cleaned_data['album'],
            music_file_data=request.FILES['music_file_data'].read()
        )

        session.add(new_song)
