from rest_framework import generics

from games.api.serializers import (PlatformSerializer, 
                                   DeveloperSerializer, 
                                   GenreSerializer, 
                                   PublisherSerializer, 
                                   GameSerializer)
from games.models import Platform, Developer, Genre, Publisher, Game


class PlatformListAPIView(generics.ListAPIView):
    """Provide a read-only view for platforms"""
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class DeveloperListAPIView(generics.ListAPIView):
    """Provide a read-only view for developers"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class GenreListAPIView(generics.ListAPIView):
    """Provide a read-only view for genres"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherListAPIView(generics.ListAPIView):
    """Provide a read-only view for publishers"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class GameListAPIView(generics.ListAPIView):
    """Provide a read-only view for games"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer


