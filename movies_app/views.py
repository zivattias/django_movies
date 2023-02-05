from django.shortcuts import render, get_object_or_404
from movies_app.models import *
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from movies_app.serializers import *

# Create your views here.


# Movies:
def movies_list(request: Request):
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


@api_view(http_method_names=["GET", "POST"])
def get_movies_list(request: Request):
    if request.method == "GET":
        return movies_list(request)
    elif request.method == "POST":
        serializer = MovieDetailsSerializer(data=request.data)
        # serializer.data
        if serializer.is_valid(raise_exception=True):
            # serializer.validated_data
            serializer.create(validated_data=serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "PATCH", "DELETE"])
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

    if request.method == "GET":
        serializer = MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)

    elif request.method == "PATCH":
        # 'partial=True' will not check if all non-null fields aren't null in request.data
        serializer = MovieDetailsSerializer(
            movie, data=request.data, many=False, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_200_OK)


# Ratings:
@api_view(http_method_names=["GET"])
def get_ratings_list(request: Request):
    ratings = Rating.objects.all()

    if "min_rating" in request.query_params:
        ratings = ratings.filter(rating__gte=request.query_params["min_rating"])
    if "max_rating" in request.query_params:
        ratings = ratings.filter(rating__lte=request.query_params["max_rating"])
    if "rating_year" in request.query_params:
        ratings = ratings.filter(rating_date__year=request.query_params["rating_year"])
    if "rating_month" in request.query_params:
        ratings = ratings.filter(
            rating_date__month=request.query_params["rating_month"]
        )
    if "rating_day" in request.query_params:
        ratings = ratings.filter(rating_date__day=request.query_params["rating_day"])
    if ("rating_from_date" in request.query_params) and (
        "rating_from_date" in request.query_params
    ):
        ratings = ratings.filter(
            rating_date__range=(
                request.query_params["rating_from_date"],
                request.query_params["rating_to_date"],
            )
        )
    else:
        if "rating_from_date" in request.query_params:
            ratings = ratings.filter(
                rating_date__gte=request.query_params["rating_from_date"]
            )
        if "rating_to_date" in request.query_params:
            ratings = ratings.filter(
                rating_date__lte=request.query_params["rating_to_date"]
            )

    if not ratings:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = RatingSerializer(instance=ratings, many=True)
    return Response(serializer.data)


# Movie actors:
@api_view(["GET", "POST"])
def movie_actors(request: Request, movie_id: int):
    if request.method == "GET":
        movie_actors = MovieActor.objects.filter(movie_id=movie_id)

        if "main_roles" in request.query_params:
            movie_actors = movie_actors.filter(main_role=True)
        if "salary_from" in request.query_params:
            movie_actors = movie_actors.filter(
                salary__gte=request.query_params["salary_from"]
            )
        if "salary_to" in request.query_params:
            movie_actors = movie_actors.filter(
                salary__lte=request.query_params["salary_to"]
            )

        if not movie_actors:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AddMovieActorSerializer(
            data=request.data,
            context={"movie_id": movie_id, "request": request},
        )

        get_object_or_404(Movie, id=movie_id)

        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


# Actors:
@api_view(["POST"])
def create_actor(request: Request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.create(validated_data=serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def manipulate_actor(request: Request, actor_id: int):
    actor = get_object_or_404(Actor, id=actor_id)
    if request.method == "GET":
        serializer = ActorSerializer(instance=actor, many=False)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = ActorSerializer(actor, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        actor.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["DELETE", "PATCH"])
def alter_movie_actor(request: Request, movie_id: int, actor_id: int):
    movieactor = get_object_or_404(MovieActor, movie_id=movie_id, actor_id=actor_id)
    if request.method == "DELETE":
        movieactor.delete()
        return Response(status=status.HTTP_200_OK)

    elif request.method == "PATCH":
        serializer = MovieActorPatchSerializer(
            movieactor, data=request.data, many=False, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)


@api_view(["POST", "GET"])
def add_movie_rating(request: Request, movie_id: int):
    if request.method == "POST":
        serializer = AddRatingSerializer(
            data=request.data, context={"movie_id": movie_id, "request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)

    if request.method == "GET":
        ratings = Rating.objects.filter(movie_id=movie_id)
        if not ratings:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SpecificMovieRatingsSerializer(instance=ratings, many=True)
        return Response(serializer.data)


@api_view(["DELETE"])
def delete_movie_rating(request: Request, movie_id: int, rating_id: int):
    rating = get_object_or_404(Rating, movie_id=movie_id, id=rating_id)
    rating.delete()
    return Response(status=status.HTTP_200_OK)


def get_homepage(request: Request):
    return render(request, "index.html")
