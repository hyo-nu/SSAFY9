from django.shortcuts import render
from django.views.decorators.http import require_safe, require_POST,require_http_methods
from .models import Movie,Genre


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
        }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie,
        }
    return render(request, 'movies/detail.html',context)

@require_safe
def recommend(request):
    genres = Genre.objects.all()
    context = {
        'genres' : genres,
        }
    return render(request, 'movies/recommend.html', context)
    
@require_safe
def recommended(request, genre_pk):
    genre = Genre.objects.get(pk=genre_pk)
    movies = Movie.objects.filter(genres=genre_pk)[:10]
    context = {
        'movies' : movies,
        'genre' : genre,
        }
    return render(request, 'movies/recommended.html', context)
    