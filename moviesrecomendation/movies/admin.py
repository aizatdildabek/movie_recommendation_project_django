from django.contrib import admin
from .models import *
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'producer', 'genre', 'release_year']
    list_editable = ['title', 'producer']
    list_per_page = 3
    list_filter = ['producer']
    search_fields = ['title']

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Producer)
admin.site.register(UserRating)
admin.site.register(UserPreference)
admin.site.register(Rating)
