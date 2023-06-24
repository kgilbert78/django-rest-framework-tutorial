from rest_framework import serializers
from .models import Album, Track

class AlbumSerializer(serializers.ModelSerializer):
    track = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'track']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'order', 'title', 'duration']