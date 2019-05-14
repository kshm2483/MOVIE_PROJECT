from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.
# DIRECTOR
class Director(models.Model):
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.director   

# GENRE
class Genre(models.Model):
    genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.genre  

class Actor(models.Model):
    actor = models.TextField()
    
    def __str__(self):
        return self.actor
    
# MOVIE
class Movie(models.Model):
    title = models.CharField(max_length=100)
    openingDate = models.DateField()
    audience = models.IntegerField()
    nationality = models.TextField()
    distributor = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE) # MOVIE랑 1:N
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)
    runningTime = models.TextField()
    movieRating = models.TextField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True) # M:N - movies
    poster_url = models.TextField()
    
    def __str__(self):
        return self.title
        
        
# Score
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # MOVIE랑 1:N 
    content = models.CharField(max_length=100)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    def __str__(self):
        return "{} {}점".format(self.content, self.score)