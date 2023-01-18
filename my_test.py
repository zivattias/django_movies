import os
import random

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import Movie, Rating

# new_movie = Movie(movie_name='AAA', description=2020, duration=124, release_year=2020)
# new_movie.save()

# Movie(movie_name='b', description=2020, duration=124, release_year=2020).save()
# Movie(movie_name='c', description=2020, duration=124, release_year=2020).save()
# Movie(movie_name='d', description=2020, duration=124, release_year=2020).save()
# Movie(movie_name='e', description=2020, duration=124, release_year=2020).save()

# all_movies = Movie.objects.all()
# total = 0
# for movie in all_movies:
#     total += movie.duration
# print(total / 60)

# for movie in Movie.objects.all():
#     Rating(movie=movie, rating=random.randint(1, 10)).save()

m = Movie.objects.get(pk=3)
print(m.rating_set.all())
