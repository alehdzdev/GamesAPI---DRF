from django.contrib import admin
from games.models import Platform, Developer, Genre, Publisher, Game

admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Game)
