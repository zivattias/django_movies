from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField,
    Serializer,
    CharField,
    PrimaryKeyRelatedField,
)
from rest_framework.fields import IntegerField, BooleanField
from movies_app.models import *

__all__ = [
    "MovieSerializer",
    "MovieDetailsSerializer",
    "RatingSerializer",
    "MovieActorSerializer",
    "AddMovieActorSerializer",
]


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["description", "actors"]
        depth = 1


class MovieDetailsSerializer(ModelSerializer):
    class Meta:
        model = Movie
        exclude = ["actors"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        depth = 1

    movie = MovieSerializer()


class ActorNameSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ["name"]


class MovieActorSerializer(ModelSerializer):
    actor = StringRelatedField(many=False)

    class Meta:
        model = MovieActor
        exclude = ["movie"]
        depth = 1


class MyActorSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(
        max_length=256, min_length=2, allow_blank=False, trim_whitespace=True
    )
    birth_year = IntegerField(max_value=2020, min_value=1900)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)


class AddMovieActorSerializer(Serializer):
    actor_id = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Actor.objects.all().values_list("id", flat=True),
    )
    salary = IntegerField(min_value=0)
    main_role = BooleanField()

    # class Meta:
    #     model = MovieActor
    #     fields = ["actor_id", "salary", "main_role"]

    def create(self, validated_data):
        MovieActor.objects.create(movie_id=self.context["movie_id"], **validated_data)
