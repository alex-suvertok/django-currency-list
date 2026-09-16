"""A library simplifying the handling of currency fields in Django projects."""

from .currency import Currency
from .fields import CurrencyField

__version__ = "0.2.0"

CurrencyChoices = Currency.CurrencyChoices

currency_code_list = Currency.currency_code_list
get_label = Currency.get_label
currency_dict = Currency.currency_dict
reversed_currency_dict = Currency.reverse_currency_dict


__all__ = [
    'Currency', 'CurrencyField', 'CurrencyChoices', '__version__',
    'currency_code_list', 'get_label', 'currency_dict', 'reversed_currency_dict'
]
