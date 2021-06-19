from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

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


class PlatformDetailAPIView(APIView):

    def get_object(self, pk):
        platform = get_object_or_404(Platform, pk=pk)
        return platform

    def get(self, request, pk):
        platform = self.get_object(pk)
        serializer = PlatformSerializer(platform)
        return Response(serializer.data)


class DeveloperListAPIView(generics.ListAPIView):
    """Provide a read-only view for developers"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperDetailAPIView(APIView):

    def get_object(self, pk):
        developer = get_object_or_404(Developer, pk=pk)
        return developer

    def get(self, request, pk):
        developer = self.get_object(pk)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)


class GenreListAPIView(generics.ListAPIView):
    """Provide a read-only view for genres"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailAPIView(APIView):

    def get_object(self, pk):
        genre = get_object_or_404(Genre, pk=pk)
        return genre

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


class PublisherListAPIView(generics.ListAPIView):
    """Provide a read-only view for publishers"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailAPIView(APIView):

    def get_object(self, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        return publisher

    def get(self, request, pk):
        publisher = self.get_object(pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)


class GameListAPIView(generics.ListAPIView):
    """Provide a read-only view for games"""
    queryset = Game.objects.all().order_by('-created_at')
    serializer_class = GameSerializer


class GameDetailAPIView(APIView):

    def get_object(self, pk):
        game = get_object_or_404(Game, pk=pk)
        return game

    def get(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
