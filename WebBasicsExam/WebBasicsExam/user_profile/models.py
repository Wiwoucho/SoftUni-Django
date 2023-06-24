from django.db import models
from django.core import validators
from .validators import starts_with_letter

class Profile(models.Model):
    first_name = models.CharField(
        max_length = 25,
        blank = False,
        null = False,
        validators = [validators.MinLengthValidator(2), starts_with_letter]
    )

    last_name = models.CharField(
        blank = False,
        null = False,
        max_length = 35,
        validators = [validators.MinLengthValidator(1), starts_with_letter]
    )

    email = models.EmailField(
        blank = False,
        null = False,
        max_length = 40

    )

    password = models.CharField(
        max_length = 20,
        blank = False,
        null = False,
        validators = [validators.MinLengthValidator(8)]
    )

    image_url = models.URLField(
        blank = True,
        null = True,
    )

    age = models.IntegerField(
        blank = True,
        null = True,
        default = 18
    )

