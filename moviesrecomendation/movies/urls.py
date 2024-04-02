from . import views
from .views import MovieCRUDView
from django.urls import path

urlpatterns = [
    path('', views.MovieListCreateView.as_view()),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
    
    path('all/', MovieCRUDView.as_view(), name='movie-list-create'),
    path('all/<int:pk>/', MovieCRUDView.as_view(), name='movie-detail-del-up'),

]