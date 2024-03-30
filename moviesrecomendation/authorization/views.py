from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authorization.models import User
from authorization.serializers import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins

from movies.forms import LoginForm

# Create your views here.


#login
class LoginView(generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"detail":"Logged in!"})
        return Response({"detail":"Error!"})

#registration

#logout
class LogoutView(generics.GenericAPIView):
    queryset = User.objects.all()
    # serializer_class = LoginSerializer

    def get(self, request):
        logout(request)
        return Response({"detail":"Logged out!"})

#reset password