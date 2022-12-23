from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters

from artists.api.serializers import (CountrySerializer, StyleSerializer,
                                     FieldSerializer, GenreSerializer,
                                     ArtistSerializer, ArtworkSerializer)
from artists.models import (Artist, Country, Style,
                            Field, Genre, Artwork)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtworkListCreate(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['year', 'genre__name', 'artist__name', ]
    search_fields = ['title', ]
    ordering_fields = ['title', 'artist', 'year', ]


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        'year_of_birth',
        'year_of_death',
        'style__name',
        'nationality__name',
        'state_of_residence__name'
    ]
    ordering_fields = ['name', 'year_of_birth']


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
