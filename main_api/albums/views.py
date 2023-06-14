from rest_framework import viewsets
from rest_framework.response import Response
from .models import Album, Track
from .serializer import AlbumSerializer, TrackSerializer


# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        albums = Album.objects.all()
        return albums
    
class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        tracks = Track.objects.all()
        return tracks
    
