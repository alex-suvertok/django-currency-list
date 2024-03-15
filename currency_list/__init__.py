"""A library simplifying the handling of currency fields in Django projects."""

from .core import Currency

CurrencyChoices = Currency.CurrencyChoices
get_all_currencies = Currency.get_all_currencies
get_label = Currency.get_label
__all__ = ['Currency', 'CurrencyChoices', 'get_all_currencies', 'get_label']
