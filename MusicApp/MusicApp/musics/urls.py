from django.urls import path, include

from MusicApp.musics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('create/', views.create_album, name='create album'),
        path('details/<int:pk>/', views.album_details, name='details album'),
        path('edit/<int:pk>/', views.edit_album, name='edit album'),
        path('delete/<int:pk>/', views.delete_album, name='delete album')
    ])),
    path('song/', include([
        path('create/', views.create_song, name='create song'),
    ])),
]
