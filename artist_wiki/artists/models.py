from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # needed for correct presentation of name in admin panel
    class Meta:
        verbose_name_plural = "Countries"


class Style(models.Model):
    name = models.CharField(max_length=20)
    time_period = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=60)
    year_of_birth = models.CharField(max_length=6)
    year_of_death = models.CharField(max_length=6)
    nationality = models.ForeignKey(Country, related_name="national_artists", on_delete=models.CASCADE)
    state_of_residence = models.ForeignKey(Country, related_name="resident_artists", on_delete=models.CASCADE)
    style = models.ManyToManyField(Style, related_name='artists', blank=True)
    # field (many-to-many)
    # # works (many-to-one)
    influenced_by = models.ManyToManyField('self', symmetrical=False, related_name='influences', blank=True, null=True)

    def __str__(self):
        return self.name
