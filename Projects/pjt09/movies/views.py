from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_safe
from .models import Movie
import random
import json

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-vote_average')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)


def recommended(request):
    movies = get_list_or_404(Movie.objects.order_by('-vote_average'))
    movies = movies[:10]
    numbers = random.randrange(1,10)
    context = {
        'movies' : movies[numbers],
    }
    return render(request, 'movies/recommended.html', context)
