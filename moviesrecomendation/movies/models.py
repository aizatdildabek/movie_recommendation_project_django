from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} - {self.genre} - {self.producer}'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_year = models.IntegerField()
    
    def __str__(self):
        return self.title

    # def calculate_average_rating(self):
    #     user_ratings = UserRating.objects.filter(movie=self)
    #     if user_ratings.exists():
    #         total_ratings = sum([rating.rating for rating in user_ratings])
    #         return total_ratings / user_ratings.count()
    #     else:
    #         return None

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    
    def __str__(self):
        return f'{self.movie} - {self.rating}'

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    
    def __str__(self):
        return f'{self.user} - {self.movie} - {self.rating}'
