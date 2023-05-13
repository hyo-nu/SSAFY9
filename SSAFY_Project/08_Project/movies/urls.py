from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommended/<int:genre_pk>/', views.recommended, name='recommended'),

]


