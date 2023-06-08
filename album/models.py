from django.db import models
from artist.models import Artist
from genre.models import Genre
from song.models import Song


class Album(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(blank=True, upload_to='images/')
    artists = models.ManyToManyField(Artist, related_name='Albums')
    songs = models.ManyToManyField(Song, related_name='albums')

    def __str__(self):
        return self.title

    @property
    def artists_name(self):
        return list(self.artists)

