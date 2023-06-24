from django.db import models
from .validators import only_letters
from django.core import validators


class Fruits(models.Model):
    name = models.CharField(
        blank = False,
        null = False,
        max_length = 30,
        validators = [validators.MinLengthValidator(2), only_letters]
    )

    image_url = models.URLField(
        blank = False,
        null = False,
    )

    description = models.TextField(
        blank = False,
        null = False,
    )

    nutrition = models.TextField(
        blank = False,
        null = False,
    )