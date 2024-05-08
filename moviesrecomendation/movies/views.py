from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.views.generic import FormView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from movies.models import Movie
from movies.serializers import MovieSerializer, UserRatingSerializer, UserPreferenceSerializer, ProducerSerializer, GenreSerializer, RatingSerializer, RatingApiSerializer
from movies.permissions import DjangoModelPermissionsWithRead
from rest_framework import permissions, authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from movies.filters import MovieFilter
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
import requests
from bs4 import BeautifulSoup

from movies.forms import LoginForm
from .models import Movie, UserRating, UserPreference, Producer, Genre, Rating

# Create your views here.
# получение рекомендации для текущего юзера
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.annotate(average_rating=Avg("user_ratings__rating"))
    serializer_class = MovieSerializer
  
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Movie.objects.all()
        else:
            user_preferences = UserPreference.objects.filter(user=user)
            if user_preferences.exists():
                preferred_genres = user_preferences.values_list('genre', flat=True)
                preferred_producers = user_preferences.values_list('producer', flat=True)
                return Movie.objects.filter(genre__in=preferred_genres, producer__in=preferred_producers)
            else:
                return Movie.objects.none()

# получение всех доступных фильмов, можно их отфильтровать и отсортировать
class MovieLisAllView(generics.ListAPIView):
    queryset = Movie.objects.annotate(average_rating=Avg("user_ratings__rating"))
    serializer_class = MovieSerializer
    # permission_classes = [permissions.DjangoModelPermissions, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ['title', 'producer']
    search_fields = ['^title', '=producer']
    ordering_fields = ['title', 'rating']   #-title - desc
    # ordering = 'description'

class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)

class MovieDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated] 

    lookup_field = 'pk'

# получение рекомендации для текущего юзера только по жанрам
class MoviesByGenreView(generics.ListAPIView):
    queryset =Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        user = self.request.user
        user_preferences = UserPreference.objects.filter(user=user)
        if user_preferences.exists():
            preferred_genres = user_preferences.values_list('genre', flat=True)
            return Movie.objects.filter(genre__in=preferred_genres)
        else:
            return Movie.objects.none()

# получение рекомендации для текущего юзера только по режиссерам
class MoviesByProducerView(generics.ListAPIView):
    queryset =Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        user = self.request.user
        user_preferences = UserPreference.objects.filter(user=user)
        if user_preferences.exists():
            preferred_producers = user_preferences.values_list('producer', flat=True)
            return Movie.objects.filter(producer__in=preferred_producers)
        else:
            return Movie.objects.none()

# for user_rating
class UserRatingCreateListView(generics.ListCreateAPIView):
    serializer_class = UserRatingSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        return UserRating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserRatingUpdateView(generics.UpdateAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [permissions.IsAuthenticated] 


# for user_preference, user создает свои предназначений
class UserPreferenceCreateView(generics.ListCreateAPIView):
    serializer_class = UserPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        # Фильтруем объекты UserPreference по текущему пользователю
        return UserPreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# for producer
class ProducerListView(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [permissions.IsAuthenticated] 

# for Genre
class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated] 
 

# for rating
class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


# def RatingApiView(self):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
#     url = 'https://www.imdb.com/chart/top/'
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200: 
#         soup = BeautifulSoup(response.text, 'html.parser')
#         film = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base")
#         movies = film.find_all("div", class_="sc-b189961a-0 hBZnfJ cli-children")
#         movie_data = []
#         for i in movies:
#             name = i.find('h3', class_='ipc-title__text').text  
#             rating = i.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text 
#             movie_data.append({'name': name, 'rating': rating})

#         serializer = RatingApiSerializer(data=movie_data, many=True)
#         if serializer.is_valid():
#             return serializer.data
#         else:
#             return Response(serializer.errors, status=400)
#     # else:
#     #     return Rating.objects.all()