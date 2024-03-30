from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Pass", widget=forms.PasswordInput)

    # class Meta:
    #     model = get_user_model()
    #     fields = ['username', 'password']