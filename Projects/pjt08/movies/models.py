from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField(default='1234-12-12')
    poster_path = models.TextField(blank=True)
    viewers = models.PositiveIntegerField(blank=True, default=1234)
    running_time = models.CharField(max_length=10, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    staffs = models.ManyToManyField(Staff, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField(validators = [MaxValueValidator(10)])
    
    def __str__(self):
        return self.title