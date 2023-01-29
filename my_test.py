import os

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

# m = Movie.objects.get(pk=3)
# print(m.rating)

# r = Rating.objects.get(pk=1)
# all_r = Rating.objects.all()[:500]
# print(r.movie_id)
# print(all_r)

# m = Movie.objects.get(pk=1)
# for rating in m.rating_set.all():
#     print(rating.rating)

# Executes an SQL query on the spot, expecting 1 result ONLY
# Movie.objects.get(movie_name='b')

# Executes an SQL query ONLY when data is accessed/iterated through Python code
# Movie.objects.all()
# Executes now:
# movies = Movie.objects.all().values_list('movie_name', 'duration')
# print(movies[2])

# movies_qs = Movie.objects.all().values_list('movie_name', 'duration')
# print(movies_qs.query)
# movies_qs = movies_qs.filter(release_year__gt=2020)
# print(movies_qs.query)
# movies_qs = movies_qs[:2]
# print(movies_qs.query)
