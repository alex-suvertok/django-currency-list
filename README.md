# django-currency-list

This library simplifies the handling of the currency field in Django projects.

## Features

- `Currency` — provides all ISO 4217 currency codes and names as `TextChoices`.
- `CurrencyField` — a ready-to-use `CharField` subclass with currency choices and max length `3`.

## Installation

```bash
pip install django-currency-list
```

## Usage

```python
from currency_list import CurrencyField, CurrencyChoices, get_label, currency_dict

# In models.py
class Product(models.Model):
    currency = CurrencyField()

# Get all currency codes
currency_codes = Currency.currency_code_list()

# Get a label for a code
get_label("USD")  # "United States Dollar"

# Full code → name mapping
currency_dict()  # {"USD": "United States Dollar", ...}
```

## Python / Django support

- Python 3.10 — 3.14
- Django 5.2 — 6.1+
