from django.shortcuts import render

from rest_framework import viewsets

from top_songs.models import Track
from top_songs.serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
