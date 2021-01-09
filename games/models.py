from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)

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
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name="genres")
    platforms = models.ManyToManyField(Platform, related_name="platforms")
    developers = models.ManyToManyField(Developer, related_name="developers")
    publishers = models.ManyToManyField(Publisher, related_name="publishers")
    
    def __str__(self):
        return self.name