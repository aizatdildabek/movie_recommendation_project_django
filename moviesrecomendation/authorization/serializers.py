from django.forms import forms
from rest_framework import serializers
from authorization.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'latitude', 'longitude']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

# class LoginSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = ['username', 'password']
#         model = User

