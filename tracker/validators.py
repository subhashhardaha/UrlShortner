from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL for this field")
    return value
