from django.db import models
from artist.models import Artist
from myuser.models import MyUser


class Playlist(models.Model):
    from song.models import Song

    title = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, upload_to='images/')
    artists = models.ManyToManyField(Artist)
    songs = models.ManyToManyField(Song)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    public = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.title
