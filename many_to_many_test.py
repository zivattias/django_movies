import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *


m = Movie.objects.get(id=3)

# Add data by objects:
# new_actor = Actor(name='Ziv', birth_year=1998)
# new_actor.save()
# ma = MovieActor(movie=m, actor=new_actor, salary=1000, main_role=False)
# ma.save()

# Add data by 'id' column:
# new_actor = Actor.objects.create(name='Noa', birth_year=1997)
# ma = MovieActor.objects.create(movie_id=m.id, actor_id=new_actor.id, salary=10000, main_role=True)

# Add data by OOP method:
# m.actors.create(name='Bruno', birth_year=2017, through_defaults={
#                 'salary': 20000, 'main_role': True})


# m2 = Movie.objects.get(id=1)
# m2.actors.add(Actor.objects.get(id=3), through_defaults={
#              'salary': 10000, 'main_role': False})

# Remove relation:
# m.actors.remove(Actor.objects.get(name__contains='Bruno'))

# Remove entity (CASCADE -- from movie_actors and actors tables):
# a = Actor.objects.get(name__contains='Bruno')
# a.delete()

# Relation sets:
# m = Movie.objects.get(id=3)
# print(m.actors.all())
# print(m.movieactor_set.all())

# a = Actor.objects.get(id=1)
# print(a.movie_set.all())


# Add movie to actor:
# new_actor = Actor.objects.create(name='Bruno', birth_year=2017)
# new_actor.movie_set.add(Movie.objects.get(id=1))