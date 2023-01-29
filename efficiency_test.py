import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *

# Separate query for each movie:
# for m in Movie.objects.all():
#     print(m, m.actors.all())

# Combined JOIN query w/ prefetch_related:
# for m in Movie.objects.all().prefetch_related('actors'):
#     print(m, m.actors.all())