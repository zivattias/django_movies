from django.shortcuts import render, get_object_or_404
from movies_app.models import *
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from movies_app.serializers import *

# Create your views here.


@api_view(http_method_names=["GET"])
def get_movies_list(request: Request):
    movies = Movie.objects.all()

    # Manual serialization:
    # result = [{'id': movie.id,
    #            'name': movie.movie_name,
    #            'description': movie.description,
    #            'duration_in_min': int(movie.duration),
    #            'release_year': movie.release_year} for movie in movies]
    # return Response(result)

    # Using ModelSerializer:
    if "name" in request.query_params:
        movies = movies.filter(movie_name__iexact=request.query_params["name"])
    if "duration_from" in request.query_params:
        movies = movies.filter(duration__gte=request.query_params["duration_from"])
    if "duration_to" in request.query_params:
        movies = movies.filter(duration__lte=request.query_params["duration_to"])
    if "description" in request.query_params:
        movies = movies.filter(
            description__icontains=request.query_params["description"]
        )

    if not movies:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data)


@api_view(http_method_names=["GET"])
def get_movie_details(request: Request, movie_id: int):
    # Manual 404:
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    # except Movie.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # serializer = MovieDetailsSerializer(movie, many=False)
    # return Response(serializer.data)

    # Shortcut get_object_or_404():
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailsSerializer(movie, many=False)
    return Response(serializer.data)
