from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from top_songs.models import Track
from top_songs.serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'artist__artistName']
    pagination_class = LimitOffsetPagination
