from wsgiref import validate
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import MyUser
from album.serializers import PlaylistSerializer
from song.serializers import SongSerializer
from album.models2 import Playlist


class UserSerializer(serializers.ModelSerializer):
    playlists = serializers.SerializerMethodField()
    likedDetails = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'created', 'liked', 'playlists', 'likedDetails')

    def get_playlists(self, obj):
        playlists = Playlist.objects.filter(created_by=obj)
        serializer = PlaylistSerializer(playlists, many=True)
        return serializer.data

    def get_likedDetails(self, obj):
        liked = obj.liked.all()
        song_serializer = SongSerializer(liked, many=True)
        return song_serializer.data

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        print(password, make_password(password))
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'created', 'liked')

