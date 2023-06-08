from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    artistdetails = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'

    def get_logo(self, instance):
        album = instance.album
        if album is not None:
            return 'http://localhost:8000/media/' + str(album.logo)
        return None
    
    def get_artistdetails(self, instance):
        artist = instance.artist
        if artist is not None:
            return {"title": artist.title, "id": artist.id}
    
    def get_album(self, instance):
        album = instance.album
        if album is not None:
            return { "id": instance.album.id, 'title': instance.album.title }
        return None
