from rest_framework import serializers

from artists.models import (Artist, Country,
                            Style, Field,
                            Genre, Artwork)


class ArtworkSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Artwork
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    influences = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    artworks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Artist
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    national_artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    resident_artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Country
        fields = "__all__"


class StyleSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    artworks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Style
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Field
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    artworks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = "__all__"
