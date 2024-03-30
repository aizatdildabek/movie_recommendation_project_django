from django.forms import forms
from rest_framework import serializers
from authorization.models import User

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['username', 'password']
        model = User