from rest_framework import viewsets

from artists.api.serializers import ArtistSerializer, CountrySerializer
from artists.models import Artist, Country


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
