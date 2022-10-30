from pyexpat import model
from django.db import models

class Genre(models.Model):
    """Model definition for Genre."""

    name = models.CharField(max_length=50)
    url = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Genre."""

        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        """Unicode representation of Genre."""
        pass


class Artist(models.Model):
    """Model definition for Artist."""

    artistName = models.CharField(max_length=100)
    artistUrl = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Artist."""

        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        """Unicode representation of Artist."""
        pass


class Track(models.Model):
    """Model definition for Track."""

    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    contentAdvisoryRating = models.CharField(max_length=50, blank=True, null=True)
    releaseDate = models.DateField()
    artworkUrl100 = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)


    class Meta:
        """Meta definition for Track."""

        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        """Unicode representation of Track."""
        return "{} by {}".format(self.name, self.artist.name)
    
