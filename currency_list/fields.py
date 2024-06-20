# fields.py
from django.db import models
from core import Currency


class CurrencyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 3
        kwargs['choices'] = Currency.choices
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Remove the default values to avoid redundancy in migrations
        if kwargs.get('max_length', None) == 3:
            del kwargs['max_length']
        if kwargs.get('choices', None) == Currency.choices:
            del kwargs['choices']
        if kwargs.get('blank', None):
            del kwargs['blank']
        if kwargs.get('null', None):
            del kwargs['null']
        return name, path, args, kwargs
