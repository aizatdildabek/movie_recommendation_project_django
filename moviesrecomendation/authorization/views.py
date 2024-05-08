from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authorization.models import User
from authorization.serializers import RegistrationSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from movies.forms import LoginForm
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
import requests

# Create your views here.
class UserCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

#registration
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # Получение координат из API
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        latitude = data.get('lat')
        longitude = data.get('lon')
        request.data['latitude'] = latitude
        request.data['longitude'] = longitude
        request.data['password'] = make_password(request.data['password'])
        print(request.data['latitude'], request.data['longitude'])
        return super().create(request, *args, **kwargs)

#login
# class LoginView(generics.GenericAPIView):

#     queryset = User.objects.all()
#     serializer_class = LoginSerializer

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return Response({"detail":"Logged in!"})
#         return Response({"detail":"Error!"})


#logout
# class LogoutView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     # serializer_class = LoginSerializer

#     def get(self, request):
#         logout(request)
#         return Response({"detail":"Logged out!"})

#reset password