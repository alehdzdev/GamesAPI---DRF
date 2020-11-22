from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name="genres")
    platforms = models.ManyToManyField(Platform, related_name="platforms")
    developer = models.ForeignKey(Developer,
                                  on_delete=models.CASCADE,
                                  related_name="developer")
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name="publisher")
    
    def __str__(self):
        return self.name