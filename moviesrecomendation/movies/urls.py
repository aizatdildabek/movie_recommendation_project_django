from . import views
from .views import MovieCRUDView
from django.urls import path

urlpatterns = [
    path('', MovieCRUDView.as_view(), name='movie-list-create'),
    path('<int:pk>/', MovieCRUDView.as_view(), name='movie-detail-del-up'),

]