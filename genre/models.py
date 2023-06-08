from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
