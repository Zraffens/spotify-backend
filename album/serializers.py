from rest_framework import serializers
from .models import Album
from .models2 import Playlist


class AlbumSerializer(serializers.ModelSerializer):
    # artistn = serializers.SerializerMethodField()
    # songsinfo = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    # def get_artistn(self, instance):
    #     list1 = []

    #     for i in instance.artists.all():
    #         list1.append(str(i.title))

    #     return list1

    # def get_songsinfo(self, instance):
    #     songs = instance.songs.all()
    #     songs_list = []
    #     if songs is not None:
    #         for song in songs:
    #             songs_list.append({"title": song.title, "id": song.id, "artist": song.artist, "liked": song.liked,
    #                               "length": song.length, "album": {"id": song.album.id, "title": song.album.title}})
    #     return songs_list


class PlaylistSerializer(serializers.ModelSerializer):
    artistn = serializers.SerializerMethodField()
    # songsinfo = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def get_artistn(self, instance):
        list1 = []

        for i in instance.artists.all():
            list1.append(str(i.title))
        return list1

    # def get_songsinfo(self, instance):
    #     songs = instance.songs.all()
    #     songs_list = []
    #     if songs is not None:
    #         for song in songs:
    #             artistdetails = song.artistdetails
    #             songs_list.append({"title": song.title, "id": song.id, "artist": song.artist, "liked": song.liked, "artistdetails": artistdetails,
    #                               "length": song.length, "album": {"id": song.album.id, "title": song.album.title}})
    #     return songs_list
