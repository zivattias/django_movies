import os
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q
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
    return Movie.objects.filter(Q(description__icontains='criminal') | Q(description__icontains='mob') | Q(description__icontains='cop'))

# Like previous, but get only movies that were released before 2010

def get_old_movies_by_kw() -> QuerySet:
    return Movie.objects.filter(Q(description__icontains='criminal') | Q(description__icontains='mob') | Q(description__icontains='cop'),
                                release_year__lt=2010)

# Get list of actors, and add amount of movies they played in (for each one)

def get_actors_list_and_movies_amnt() -> list[list[Actor, int]]:
    ...


if __name__ == "__main__":
    # print(get_actors_younger_than_50())
    # print(get_short_movies_later_than_2005())
    # print(get_movies_by_kw())
    # print(get_old_movies_by_kw())
    ...