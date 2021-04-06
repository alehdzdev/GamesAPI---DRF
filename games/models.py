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
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='covers')
    genres = models.ManyToManyField(Genre, related_name="genres")
    platforms = models.ManyToManyField(Platform, related_name="platforms")
    developers = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="developers")
    publishers = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="publishers")
    
    def __str__(self):
        return self.name