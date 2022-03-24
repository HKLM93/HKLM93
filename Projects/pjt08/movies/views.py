from django.views.decorators.csrf import requires_csrf_token
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, StaffListSerializer, StaffSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Movie, Review, Staff
from django.shortcuts import get_list_or_404, get_object_or_404

from movies import serializers
# Create your views here.
def get_serializer_all(request, attr, method, pk=0):
    if method == 'GET':
        if attr == 'actor':
            actors = get_list_or_404(Actor)
            serializer = ActorListSerializer(actors, many=True)
        elif attr == 'movie':
            movies = get_list_or_404(Movie)
            serializer = MovieListSerializer(movies, many=True)
        elif attr == 'staff':
            staffs = get_list_or_404(Staff)
            serializer = StaffListSerializer(staffs, many=True)
        elif attr == 'review':
            reviews = get_list_or_404(Review, pk=pk)
            serializer = ReviewListSerializer(reviews, many=True)

        return Response(serializer.data)

    elif method == 'POST':
        if attr == 'actor':
            serializer = ActorListSerializer(data=request.data)
        elif attr == 'movie':
            serializer = MovieListSerializer(data=request.data)
        elif attr == 'staff':
            serializer = StaffListSerializer(data=request.data)
        elif attr == 'review':
            movie = get_object_or_404(Movie, pk=pk)
            serializer = ReviewListSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

def get_serializer_detail(request, attr, method, pk):
    if method == 'GET':
        if attr == 'actor':
            actor = get_object_or_404(Actor, pk=pk)
            serializer = ActorSerializer(actor)
        elif attr == 'movie':
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(movie)
        elif attr == 'staff':
            staff = get_object_or_404(Staff, pk=pk)
            serializer = StaffSerializer(staff)
        elif attr == 'review':
            review = get_object_or_404(Review, pk=pk)
            serializer = ReviewSerializer(review)

        return Response(serializer.data)

    elif method == 'PUT':
        if attr == 'actor':
            actor = get_object_or_404(Actor, pk=pk)
            serializer = ActorSerializer(actor, data=request.data)
        elif attr == 'movie':
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
        elif attr == 'staff':
            staff = get_object_or_404(Staff, pk=pk)
            serializer = StaffSerializer(staff, data=request.data)
        elif attr == 'review':
            review = get_object_or_404(Review, pk=pk)
            serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif method == 'DELETE':
        if attr == 'actor':
            actor = get_object_or_404(Actor, pk=pk)
            actor.delete()
        elif attr == 'movie':
            movie = get_object_or_404(Movie, pk=pk)
            movie.delete()
        elif attr == 'staff':
            staff = get_object_or_404(Staff, pk=pk)
            staff.delete()
        elif attr == 'review':
            review = get_object_or_404(Review, pk=pk)
            review.delete()

        return Response({'message': 'delete success'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def get_actor_all(request):
    return get_serializer_all(request, 'actor', request.method)


@api_view(['GET', 'PUT', 'DELETE'])
def get_actor_detail(request, actor_pk):
    return get_serializer_detail(request, 'actor', request.method, actor_pk)


@api_view(['GET', 'POST'])
def get_movie_all(request):
    return get_serializer_all(request, 'movie', request.method)


@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_detail(request, movie_pk):
    return get_serializer_detail(request, 'movie', request.method, movie_pk)


@api_view(['GET', 'POST'])
def get_review_all(request, movie_pk):
    return get_serializer_all(request, 'review', request.method, movie_pk)


@api_view(['GET', 'PUT', 'DELETE'])
def get_review_detail(request, review_pk):
    return get_serializer_detail(request, 'review', request.method, review_pk)


@api_view(['GET', 'POST'])
def get_staff_all(request):
    return get_serializer_all(request, 'staff', request.method)


@api_view(['GET', 'PUT', 'DELETE'])
def get_staff_detail(request, staff_pk):
    return get_serializer_detail(request, 'staff', request.method, staff_pk)