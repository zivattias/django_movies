from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    movie_name = models.CharField(db_column='movie_name', max_length=256, null=False)
    description = models.TextField(db_column='description', null=False)
    duration = models.FloatField(db_column='duration', null=False)
    release_year = models.IntegerField(db_column='year', null=False,
                                       validators=[MinValueValidator(1900), MaxValueValidator(2050)])
    pic_url = models.URLField(db_column='pic_url', max_length=512, null=True)

    class Meta:
        db_table = 'movies'


class Rating(models.Model):

    movie = models.ForeignKey("Movie", on_delete=models.RESTRICT)
    rating = models.SmallIntegerField(db_column='rating', null=False, validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(11)])

    class Meta:
        db_table = 'ratings'
