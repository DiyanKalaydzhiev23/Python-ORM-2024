from django.shortcuts import render, redirect
from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.forms import SongCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MusicApp.musics.models import Album
from MusicApp.settings import session


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        "albums": albums,
    }

    return render(request, 'common/index.html', context)


def create_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'albums/create-album.html', context)


@session_decorator(session)
def edit_album(request, pk: int):
    album = (
        session.query(Album)
        .filter(Album.id == pk)
        .first()
    )

    if request.method == "GET":
        form = AlbumEditForm(initial={
            "album_name": album.album_name,
            "image_url": album.image_url,
            "price": album.price,
        })
    else:
        form = AlbumEditForm(request.POST)

        if form.is_valid():
            form.save(album)
            return redirect('index')

    context = {
        "album": album,
        "form": form
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk: int):
    album = (
        session.query(Album)
        .filter(Album.id == pk)
        .first()
    )

    if request.method == "GET":
        form = AlbumDeleteForm(initial={
            "album_name": album.album_name,
            "image_url": album.image_url,
            "price": album.price,
        })
    else:
        session.delete(album)
        return redirect('index')

    context = {
        "album": album,
        "form": form
    }

    return render(request, 'albums/delete-album.html', context)


@session_decorator(session)
def album_details(request, pk: int):
    album = (
        session.query(Album)
        .filter(Album.id == pk)
        .first()
    )

    context = {
        "album": album,
    }

    return render(request, 'albums/album-details.html', context)


def create_song(request):

    if request.method == "GET":
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'songs/create-song.html', context)







