from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Producer)
admin.site.register(UserRating)
admin.site.register(UserPreference)
admin.site.register(Rating)
