# encoding: utf-8
from django.forms import ValidationError


class FQValidationError(ValidationError):
    pass