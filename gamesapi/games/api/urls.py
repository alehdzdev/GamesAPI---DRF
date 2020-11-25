from django.urls import include, path
from games.api import views as gv

urlpatterns = [
    path("platforms/", gv.PlatformListAPIView.as_view(),name="platforms-list"),
    path("developers/", gv.DeveloperListAPIView.as_view(),name="developers-list"),
    path("developers/<pk>/", gv.DeveloperDetailAPIView.as_view(),name="developer-detail"),
    path("genres/", gv.GenreListAPIView.as_view(),name="genres-list"),
    path("publisher/", gv.PublisherListAPIView.as_view(),name="publishers-list"),
    path("games/", gv.GameListAPIView.as_view(),name="games-list"),
]