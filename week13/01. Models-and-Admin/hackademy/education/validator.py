from django.core.exceptions import ValidationError


def validate_url(value):
    if 'https://github.com/' not in str(value):
        raise ValidationError(f'{value} is not a valid url. It should have github domain.')
