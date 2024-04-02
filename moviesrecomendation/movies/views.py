from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.views.generic import FormView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.permissions import DjangoModelPermissionsWithRead
from rest_framework import permissions, authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins

from movies.forms import LoginForm

@login_required
def index(request):
    return HttpResponse("HELLO AIZAT")

# Create your views here.
class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    # authentication_classes = [authentication.SessionAuthentication] settings добавили rest_framework-session authenticatication, теперь работает автоматический по умолчаню, но здесь можем изменить
    # permission_classes = [DjangoModelPermissionsWithRead]
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'



class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'


class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'






# for Movie with mixins
class MovieCRUDView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    """
    Retrieve - Чтение одной записи по айди - GET
    List - чтение списка записей - GET
    Create - создание
    Destroy - Удаление
    Update - обновление по айди

    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):  # keyword arguments
        print("kwargs: ", kwargs)
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
