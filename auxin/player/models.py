from django.db import models

# Create your models here.

class Albums(models.Model):
    """
    Model for storing Albums
    """

    album_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Songs(models.Model):
    """
    Model for storing all the songs corresponding to an album
    """

    album_name = models.ForeignKey(Albums, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)