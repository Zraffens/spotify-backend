from .models import Album
from .models2 import Playlist
from song.models import Song
from .serializers import AlbumSerializer, PlaylistSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
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
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        public_playlists = Playlist.objects.filter(public=True)
        user_playlists = Playlist.objects.none()
        if user.is_authenticated:
            user_playlists = Playlist.objects.filter(created_by=user)

        queryset = public_playlists.union(user_playlists)
        return queryset


class UserPlaylists(generics.ListCreateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Playlist.objects.filter(created_by=self.request.user)
        return queryset


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


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
        title = self.kwargs['title'].lower()
        print(title)
        return Album.objects.filter(title__contains=title)


class PlaylistCreate(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = PlaylistSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
