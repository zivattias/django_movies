from rest_framework.serializers import ModelSerializer
from movies_app.models import *

__all__ = [
    'MovieSerializer',
    'MovieDetailsSerializer'
]

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['description', 'actors']
        depth = 1


class MovieDetailsSerializer(ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']
