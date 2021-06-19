from django.urls import path
from games.api import views as gv

urlpatterns = [
    path("platforms/", gv.PlatformListAPIView.as_view(), name="platforms-list"),
    path("platforms/<pk>/", gv.PlatformDetailAPIView.as_view(), name="platforms-detail"),
    path("developers/", gv.DeveloperListAPIView.as_view(), name="developers-list"),
    path("developers/<pk>/", gv.DeveloperDetailAPIView.as_view(), name="developers-detail"),
    path("genres/", gv.GenreListAPIView.as_view(), name="genres-list"),
    path("genres/<pk>/", gv.GenreDetailAPIView.as_view(), name="genres-detail"),
    path("publishers/", gv.PublisherListAPIView.as_view(), name="publishers-list"),
    path("publishers/<pk>/", gv.PublisherDetailAPIView.as_view(), name="publishers-detail"),
    path("games/", gv.GameListAPIView.as_view(), name="games-list"),
    path("games/<pk>/", gv.GameDetailAPIView.as_view(), name="game-detail"),
]
