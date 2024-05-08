from django.forms import forms
from rest_framework import serializers
from movies.models import Movie, UserRating, UserPreference, User, Genre, Producer, Rating

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Movie
        fields = ['title', 'producer', 'genre', 'release_year', 'images','average_rating']


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = ['movie', 'rating']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class UserPreferenceSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = UserPreference
        fields = ['genre', 'producer']

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['name', 'email', 'city', 'country']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['movie', 'rating']

class RatingApiSerializer(serializers.Serializer):
    name = serializers.CharField()
    rating = serializers.CharField()

