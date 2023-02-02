from django.urls import path
from . import views

urlpatterns = [
    path("movies", views.get_movies_list),
    path("movies/<int:movie_id>", views.get_movie_details),
    path("movies/<int:movie_id>/actors", views.movie_actors),
    path("movies/<int:movie_id>/actors/<int:actor_id>", views.alter_movie_actor),
    path("movies/<int:movie_id>/ratings", views.add_movie_rating),
    path("movies/<int:movie_id>/ratings/<int:rating_id>", views.delete_movie_rating),
    path("actors", views.create_actor),
    path("actors/<int:actor_id>", views.manipulate_actor),
    path("ratings", views.get_ratings_list),
]
