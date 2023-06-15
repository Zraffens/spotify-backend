from rest_framework import serializers
from .models import Album
from .models2 import Playlist


class AlbumSerializer(serializers.ModelSerializer):
    artistn = serializers.SerializerMethodField()
    songsinfo = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    def get_artistn(self, instance):
        list1 = []

        for i in instance.artists.all():
            list1.append(str(i.title))

        return list1

    def get_songsinfo(self, instance):
        songs = instance.songs.all()
        MEDIA_DIR = 'http://localhost:8000/media/'
        songs_list = []
        if songs is not None:
            for song in songs:
                artist = song.artist
                artistdetails = {"id": artist.id, "title": artist.title}
                det =  {"id": artistdetails["id"], "title": artistdetails["title"]}
                songs_list.append({"title": song.title, "id": song.id, "liked": song.liked, "artistdetails": det, "file": MEDIA_DIR + str(song.file), "logo": MEDIA_DIR + str(song.album.logo),
                                  "length": song.length, "album": {"id": song.album.id, "title": song.album.title}})
        return songs_list


class PlaylistSerializer(serializers.ModelSerializer):
    artistn = serializers.SerializerMethodField()
    songsinfo = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def get_artistn(self, instance):
        list1 = []

        for i in instance.artists.all():
            list1.append(str(i.title))
        return list1

    def get_songsinfo(self, instance):
        songs = instance.songs.all()
        MEDIA_DIR = 'http://localhost:8000/media/'
        songs_list = []
        if songs is not None:
            for song in songs:
                artist = song.artist
                artistdetails = {"id": artist.id, "title": artist.title}
                det =  {"id": artistdetails["id"], "title": artistdetails["title"]}
                songs_list.append({"title": song.title, "id": song.id, "artistdetails": det, "file": MEDIA_DIR + str(song.file), "logo": MEDIA_DIR + str(song.album.logo),
                                  "length": song.length, "album": {"id": song.album.id, "title": song.album.title}})
        return songs_list
    
    def get_username(self, instance):
        return instance.created_by.username
