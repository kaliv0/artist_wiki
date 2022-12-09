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
    # artworks = ArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    # national_artists = ArtistSerializer(many=True, read_only=True)
    # resident_artists = ArtistSerializer(many=True, read_only=True)
    national_artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    resident_artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Country
        fields = "__all__"


class StyleSerializer(serializers.ModelSerializer):
    # artists = ArtistSerializer(many=True, read_only=True)
    # artworks = ArtworkSerializer(many=True, read_only=True)
    artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    artworks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Style
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    # artists = ArtistSerializer(many=True, read_only=True)
    artists = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Field
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    # artworks = ArtworkSerializer(many=True, read_only=True)
    artworks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = "__all__"
