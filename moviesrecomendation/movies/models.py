from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
# Create your models here.

class Producer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class UserPreference(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return f'{self.user} - {self.genre}'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_year = models.IntegerField()
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MaxValueValidator(10)])
    
    def __str__(self):
        return f'{self.movie} - {self.rating}'

class UserRating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='user_ratings')
    rating = models.FloatField(validators=[MaxValueValidator(10)])
    
    def __str__(self):
        return f'{self.user} - {self.movie} - {self.rating}'
