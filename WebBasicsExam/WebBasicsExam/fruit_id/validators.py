from django.core.exceptions import ValidationError


def only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should only contain letters!')

