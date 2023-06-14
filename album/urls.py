from django.urls import path
from .views import AlbumDetail, AlbumList, PlaylistList, PlaylistDetail, AlbumSongList, AlbumSearchList, PlaylistCreate, UserPlaylists

urlpatterns = [
    path('albums/', AlbumList.as_view()),
    path('albums/<int:pk>', AlbumDetail.as_view()),
    path('playlists/', PlaylistList.as_view()),
    path('playlists-create/', PlaylistCreate.as_view(), name='playlist-create'),
    path('playlists/<int:pk>', PlaylistDetail.as_view()),
    path('userplaylists/', UserPlaylists.as_view()),
    path('getsongs/<int:id>', AlbumSongList.as_view()),
    path('filter/<str:title>/', AlbumSearchList.as_view()),
]
