from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    songsinfo = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = '__all__'

    def get_songsinfo(self, instance):
        songs = instance.song_set.all()
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
