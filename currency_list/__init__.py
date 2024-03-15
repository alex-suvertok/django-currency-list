"""A library simplifying the handling of currency fields in Django projects."""

from .core import Currency

CurrencyChoices = Currency.CurrencyChoices
currency_code_list = Currency.currency_code_list
get_label = Currency.get_label
currency_dict = Currency.currency_dict

__all__ = ['Currency', 'CurrencyChoices', 'currency_code_list', 'get_label', 'currency_dict']
