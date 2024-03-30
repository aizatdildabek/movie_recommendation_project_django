from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from authorization.managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    SUPERUSER, MODERATOR, APPUSER = 1, 2, 3

    ROLES = (
        (SUPERUSER, 'Superuser'),
        (MODERATOR, 'Moderator'),
        (APPUSER, 'AppUser'),
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True) #blank-не обязательно, null-разрешено пустое значение
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    role = models.IntegerField(default=APPUSER, choices=ROLES)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True) #юзер активен или нет, поум - да
    is_staff = models.BooleanField(default=False) #есть ли доступ к админ панели, фолс - доступ нет
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []