from django.db import models
from artist.models import Artist
from django.db.models.signals import pre_save
import mutagen


class Song(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='musics/', null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    liked = models.BooleanField(default=False)
    length = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def album(self):
        return self.albums.first() if self.albums.exists() else None
    
    
'''from django.db import models
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    liked = models.BooleanField(default=False)
    length = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title'''


def get_length(sender, instance, raw, using, update_fields, **kwargs):
    # read audio file metadata
    audio_info = mutagen.File(instance.file).info
    # set audio duration in seconds, so we can access it in database
    instance.length = int(audio_info.length)


pre_save.connect(get_length, sender=Song)
