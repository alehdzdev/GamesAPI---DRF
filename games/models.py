from django.db import models


class Platform(models.Model):
    GENERATIONS = [
        ('1st', 'First generation'),
        ('2nd', 'Second generation'),
        ('3rd', 'Third generation'),
        ('4th', 'Fourth generation'),
        ('5th', 'Fifth generation'),
        ('6th', 'Sixth generation'),
        ('7nd', 'Seventh generation'),
        ('8rd', 'Eighth generation'),
        ('9th', 'Ninth generation'),
    ]
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    generation = models.CharField(max_length=4, choices=GENERATIONS, null=True, blank=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='covers', default='media/covers/not_image.png')
    genres = models.ManyToManyField(Genre, related_name="genres")
    platforms = models.ManyToManyField(Platform, related_name="platforms")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="developer", blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="publisher", blank=True, null=True)

    def __str__(self):
        return self.name
