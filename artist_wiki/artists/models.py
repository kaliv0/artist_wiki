from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Style(models.Model):
    name = models.CharField(max_length=30)
    time_period = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=60)
    year_of_birth = models.CharField(max_length=8, null=True, blank=True)
    year_of_death = models.CharField(max_length=8, null=True, blank=True)
    nationality = models.ForeignKey(Country,
                                    related_name="national_artists",
                                    on_delete=models.CASCADE)
    state_of_residence = models.ForeignKey(Country, null=True, blank=True,
                                           related_name="resident_artists",
                                           on_delete=models.CASCADE)
    style = models.ManyToManyField(Style, related_name='artists', blank=True)
    field = models.ManyToManyField(Field, related_name='artists', blank=True)
    influenced_by = models.ManyToManyField('self', symmetrical=False,
                                           related_name='influences', blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=8, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True,
                               related_name='artworks',
                               on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='artworks', blank=True)
    style = models.ManyToManyField(Style, related_name='artworks', blank=True)

    def __str__(self):
        return self.title
