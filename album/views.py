from .models import Album
from .models2 import Playlist
from song.models import Song
from .serializers import AlbumSerializer, PlaylistSerializer
from rest_framework import mixins
from rest_framework import generics
import json
from django.http import HttpResponse
from song.serializers import SongSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# def AlbumSongList(response, id, *args, **kwargs):
#     queryset = Song.objects.filter(album__id=id)
#     return HttpResponse(json.dumps(queryset))

class AlbumSongList(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Song.objects.filter(album__id=id)


class AlbumSearchList(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        title = self.kwargs['title'].lower()
        print(title)
        return Album.objects.filter(title__contains=title)
