from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.movie_list, name='movie_list'),
    # path('<int:pk>/', views.movie_detail, name='detail'),

    path('', views.MovieListView.as_view()),
    path('<int:pk>/', views.MovieDetailUpdateDeleteView.as_view()),
    path('all/', views.MovieLisAllView.as_view()),
    path('producers/', views.ProducerListView.as_view()),
    path('genres/', views.GenreListView.as_view()),
    path('by-genres/', views.MoviesByGenreView.as_view()),
    path('by-producers/', views.MoviesByProducerView.as_view()),
    path('preferences/', views.UserPreferenceCreateView.as_view()),
    path('rating/', views.UserRatingCreateListView.as_view()),
    path('rating/update/', views.UserRatingUpdateView.as_view()),
    path('rating-api/', views.RatingListView.as_view()),


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









    # path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
    # path('create/', views.MovieCreateView.as_view(), name='create'),
    # path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='delete'),