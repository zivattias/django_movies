import os
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q, FloatField
from django.db.models.aggregates import Avg, Min, Max, Count
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *

# Get actors younger than 50 years old


def get_actors_younger_than_50() -> QuerySet:
    min_year = datetime.now().year - 50
    return Actor.objects.filter(birth_year__gt=min_year)


# Get movies that last less than 2.5 hours and were released after 2005


def get_short_movies_later_than_2005() -> QuerySet:
    mins = 2.5 * 60
    min_release_year = 2006
    return Movie.objects.filter(duration__lt=mins, release_year__gte=min_release_year)


# Get all the movies that contain a word “criminal”, “mob” or “cop” in their description


def get_movies_by_kw() -> QuerySet:
    return Movie.objects.filter(
        Q(description__icontains="criminal")
        | Q(description__icontains="mob")
        | Q(description__icontains="cop")
    )


# Like previous, but get only movies that were released before 2010


def get_old_movies_by_kw() -> QuerySet:
    return Movie.objects.filter(
        Q(description__icontains="criminal")
        | Q(description__icontains="mob")
        | Q(description__icontains="cop"),
        release_year__lt=2010,
    )


# Get list of actors, and add amount of movies they played in (for each one)


def get_actors_list_and_movies_amnt() -> list[list[Actor, int]]:
    actors = Actor.objects.annotate(num_movies=Count("movieactor__movie"))
    return [(actor.name, actor.num_movies) for actor in actors]


# Get average, min, and max rating in the system


def get_aggregated_ratings() -> dict[str, float]:
    return Rating.objects.aggregate(
        min=Min("rating", output_field=FloatField()),
        max=Max("rating", output_field=FloatField()),
        avg=Avg("rating", output_field=FloatField()),
    )


# Get Movies with their avg ratings


def get_movies_and_avg_ratings() -> list[tuple[str, float]]:
    movies = Movie.objects.annotate(avg_rating=Avg("rating__rating"))
    return [(movie.movie_name, movie.avg_rating) for movie in movies]


# Get ratings that were created in 2023


def get_ratings_before_2023() -> QuerySet:
    return Rating.objects.filter(rating_date__year__lt=2023)


# Get all the actors in the system with min and max rating of the movies they played in


def get_actors_min_max_rating() -> list[tuple[str, int]]:
    actors = Actor.objects.annotate(
        min_rating=Min("movie__rating__rating"), max_rating=Max("movie__rating__rating")
    )
    return [(actor.name, actor.min_rating, actor.max_rating) for actor in actors]


# Get movies with average salary for actors in each one


def get_movies_with_avg_salary() -> list[tuple[str, float]]:
    movies = Movie.objects.annotate(
        avg_salary=Avg("movieactor__salary", output_field=FloatField())
    )
    return [(movie.movie_name, movie.avg_salary) for movie in movies]


# Get actors with their average salaries


def get_actors_avg_salary() -> list[tuple[str, float]]:
    actors = Actor.objects.annotate(
        avg_salary=Avg("movieactor__salary", output_field=FloatField())
    )
    return [(actor.name, actor.avg_salary) for actor in actors]


# Get actors who played main roles at least once


def get_atleast_once_main_actors() -> list[str]:
    actors = Actor.objects.filter(movieactor__main_role=True)
    return [actor.name for actor in actors]


# Get movies and amount of actors who played main roles


def get_movies_and_main_actors_amnt() -> list[tuple[str, int]]:
    movies = Movie.objects.filter(movieactor__main_role=True).annotate(
        main_actors_amnt=Count("movieactor__actor_id")
    )
    return [(movie.movie_name, movie.main_actors_amnt) for movie in movies]


if __name__ == "__main__":
    print(get_actors_younger_than_50())
    print(get_short_movies_later_than_2005())
    print(get_movies_by_kw())
    print(get_old_movies_by_kw())
    print(get_actors_list_and_movies_amnt())
    print(get_aggregated_ratings())
    print(get_movies_and_avg_ratings())
    print(get_ratings_before_2023())
    print(get_actors_min_max_rating())
    print(get_movies_with_avg_salary())
    print(get_actors_avg_salary())
    print(get_atleast_once_main_actors())
    print(get_movies_and_main_actors_amnt())
