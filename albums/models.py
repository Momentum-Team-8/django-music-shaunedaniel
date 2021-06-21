from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album_art = models.CharField(max_length=255)
