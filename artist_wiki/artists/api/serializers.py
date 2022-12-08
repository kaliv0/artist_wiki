from rest_framework import serializers

from artists.models import Artist, Country


class ArtistSerializer(serializers.ModelSerializer):
    influences = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Artist
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    national_artists = ArtistSerializer(many=True, read_only=True)
    resident_artists = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = "__all__"
