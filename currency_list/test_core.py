import pytest

from .currency import Currency


def test_currency_code_list():
    expected_currencies = [
        'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
        'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
        'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
        'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP',
        'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS',
        'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
        'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY',
        'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KPW', 'KWD', 'KYD', 'KZT', 'LAK',
        'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK',
        'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD',
        'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
        'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD',
        'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN',
        'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD',
        'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV',
        'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW'
    ]
    assert Currency.currency_code_list() == expected_currencies


@pytest.mark.parametrize("code, expected_label", [
    ('USD', 'United States Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound Sterling'),
])
def test_get_label(code, expected_label):
    assert Currency.get_label(code) == expected_label


def test_currency_dict():
    expected_dict = {
        'AED': 'United Arab Emirates Dirham',
        'AFN': 'Afghan Afghani',
        'ALL': 'Albanian Lek',
        'AMD': 'Armenian Dram',
        'ANG': 'Netherlands Antillean Guilder',
        'AOA': 'Angolan Kwanza',
        'ARS': 'Argentine Peso',
        'AUD': 'Australian Dollar',
        'AWG': 'Aruban Florin',
        'AZN': 'Azerbaijani Manat',
        'BAM': 'Bosnia-Herzegovina Convertible Mark',
        'BBD': 'Barbadian Dollar',
        'BDT': 'Bangladeshi Taka',
        'BGN': 'Bulgarian Lev',
        'BHD': 'Bahraini dinar',
        'BIF': 'Burundian Franc',
        'BMD': 'Bermudian Dollar',
        'BND': 'Brunei Dollar',
        'BOB': 'Bolivian Boliviano',
        'BRL': 'Brazilian Real',
        'BSD': 'Bahamian Dollar',
        'BTN': 'Bhutanese Ngultrum',
        'BWP': 'Botswana Pula',
        'BYN': 'Belarusian Ruble',
        'BZD': 'Belize Dollar',
        'CAD': 'Canadian Dollar',
        'CDF': 'Congolese Franc',
        'CHF': 'Swiss Franc',
        'CLP': 'Chilean Peso',
        'CNY': 'Chinese Yuan',
        'COP': 'Colombian Peso',
        'CRC': 'Costa Rican Colon',
        'CUP': 'Cuban Peso',
        'CVE': 'Cape Verdean Escudo',
        'CZK': 'Czech Koruna',
        'DJF': 'Djiboutian Franc',
        'DKK': 'Danish Krone',
        'DOP': 'Dominican Peso',
        'DZD': 'Algerian Dinar',
        'EGP': 'Egyptian Pound',
        'ERN': 'Eritrean Nakfa',
        'ETB': 'Ethiopian Birr',
        'EUR': 'Euro',
        'FJD': 'Fijian Dollar',
        'FKP': 'Falkland Islands Pound',
        'FOK': 'Faroese Króna',
        'GBP': 'British Pound Sterling',
        'GEL': 'Georgian Lari',
        'GGP': 'Guernsey Pound',
        'GHS': 'Ghanaian Cedi',
        'GIP': 'Gibraltar Pound',
        'GMD': 'Gambian Dalasi',
        'GNF': 'Guinean Franc',
        'GTQ': 'Guatemalan Quetzal',
        'GYD': 'Guyanaese Dollar',
        'HKD': 'Hong Kong Dollar',
        'HNL': 'Honduran Lempira',
        'HRK': 'Croatian Kuna',
        'HTG': 'Haitian Gourde',
        'HUF': 'Hungarian Forint',
        'IDR': 'Indonesian Rupiah',
        'ILS': 'Israeli New Shekel',
        'IMP': 'Manx Pound',
        'INR': 'Indian Rupee',
        'IQD': 'Iraqi Dinar',
        'IRR': 'Iranian Rial',
        'ISK': 'Icelandic Króna',
        'JMD': 'Jamaican Dollar',
        'JOD': 'Jordanian Dinar',
        'JPY': 'Japanese Yen',
        'KES': 'Kenyan Shilling',
        'KGS': 'Kyrgystani Som',
        'KHR': 'Cambodian Riel',
        'KID': 'Kiribati Dollar',
        'KMF': 'Comorian Franc',
        'KPW': 'South Korean Won',
        'KWD': 'Kuwaiti Dinar',
        'KYD': 'Cayman Islands Dollar',
        'KZT': 'Kazakhstani Tenge',
        'LAK': 'Laotian Kip',
        'LBP': 'Lebanese Pound',
        'LKR': 'Sri Lankan Rupee',
        'LRD': 'Liberian Dollar',
        'LSL': 'Lesotho Loti',
        'LYD': 'Libyan Dinar',
        'MAD': 'Moroccan Dirham',
        'MDL': 'Moldovan Leu',
        'MGA': 'Malagasy Ariary',
        'MKD': 'Macedonian Denar',
        'MMK': 'Myanmar Kyat',
        'MNT': 'Mongolian Tugrik',
        'MOP': 'Macanese Pataca',
        'MRU': 'Mauritanian Ouguiya',
        'MUR': 'Mauritian Rupee',
        'MVR': 'Maldivian Rufiyaa',
        'MWK': 'Malawian Kwacha',
        'MXN': 'Mexican Peso',
        'MYR': 'Malaysian Ringgit',
        'MZN': 'Mozambican Metical',
        'NAD': 'Namibian Dollar',
        'NGN': 'Nigerian Naira',
        'NIO': 'Nicaraguan Córdoba',
        'NOK': 'Norwegian Krone',
        'NPR': 'Nepalese Rupee',
        'NZD': 'New Zealand Dollar',
        'OMR': 'Omani Rial',
        'PAB': 'Panamanian Balboa',
        'PEN': 'Peruvian Nuevo Sol',
        'PGK': 'Papua New Guinean Kina',
        'PHP': 'Philippine Peso',
        'PKR': 'Pakistani Rupee',
        'PLN': 'Polish Zloty',
        'PYG': 'Paraguayan Guarani',
        'QAR': 'Qatari Rial',
        'RON': 'Romanian Leu',
        'RSD': 'Serbian Dinar',
        'RUB': 'Russian Ruble',
        'RWF': 'Rwandan Franc',
        'SAR': 'Saudi Riyal',
        'SBD': 'Solomon Islands Dollar',
        'SCR': 'Seychellois Rupee',
        'SDG': 'Sudanese Pound',
        'SEK': 'Swedish Krona',
        'SGD': 'Singapore Dollar',
        'SHP': 'Saint Helena Pound',
        'SLL': 'Sierra Leonean Leone',
        'SOS': 'Somali Shilling',
        'SRD': 'Surinamese Dollar',
        'SSP': 'South Sudanese Pound',
        'STN': 'São Tomé and Príncipe Dobra',
        'SYP': 'Syrian Pound',
        'SZL': 'Swazi Lilangeni',
        'THB': 'Thai Baht',
        'TJS': 'Tajikistani Somoni',
        'TMT': 'Turkmenistani Manat',
        'TND': 'Tunisian Dinar',
        'TOP': 'Tongan Paʻanga',
        'TRY': 'Turkish Lira',
        'TTD': 'Trinidad and Tobago Dollar',
        'TVD': 'Tuvaluan Dollar',
        'TWD': 'New Taiwan Dollar',
        'TZS': 'Tanzanian Shilling',
        'UAH': 'Ukrainian Hryvnia',
        'UGX': 'Ugandan Shilling',
        'USD': 'United States Dollar',
        'UYU': 'Uruguayan Peso',
        'UZS': 'Uzbekistan Som',
        'VES': 'Venezuelan Bolívar',
        'VND': 'Vietnamese Dong',
        'VUV': 'Vanuatu Vatu',
        'WST': 'Samoan Tala',
        'XAF': 'Central African Franc',
        'XCD': 'East Caribbean Dollar',
        'XOF': 'West African Franc',
        'XPF': 'CFP Franc',
        'YER': 'Yemeni Rial',
        'ZAR': 'South African Rand',
        'ZMW': 'Zambian Kwacha',
    }

    actual_dict = Currency.currency_dict()

    assert actual_dict == expected_dict


def test_reverse_currency_dict():
    expected_dict = {
        'United Arab Emirates Dirham': 'AED',
        'Afghan Afghani': 'AFN',
        'Albanian Lek': 'ALL',
        'Armenian Dram': 'AMD',
        'Netherlands Antillean Guilder': 'ANG',
        'Angolan Kwanza': 'AOA',
        'Argentine Peso': 'ARS',
        'Australian Dollar': 'AUD',
        'Aruban Florin': 'AWG',
        'Azerbaijani Manat': 'AZN',
        'Bosnia-Herzegovina Convertible Mark': 'BAM',
        'Barbadian Dollar': 'BBD',
        'Bangladeshi Taka': 'BDT',
        'Bulgarian Lev': 'BGN',
        'Bahraini dinar': 'BHD',
        'Burundian Franc': 'BIF',
        'Bermudian Dollar': 'BMD',
        'Brunei Dollar': 'BND',
        'Bolivian Boliviano': 'BOB',
        'Brazilian Real': 'BRL',
        'Bahamian Dollar': 'BSD',
        'Bhutanese Ngultrum': 'BTN',
        'Botswana Pula': 'BWP',
        'Belarusian Ruble': 'BYN',
        'Belize Dollar': 'BZD',
        'Canadian Dollar': 'CAD',
        'Congolese Franc': 'CDF',
        'Swiss Franc': 'CHF',
        'Chilean Peso': 'CLP',
        'Chinese Yuan': 'CNY',
        'Colombian Peso': 'COP',
        'Costa Rican Colon': 'CRC',
        'Cuban Peso': 'CUP',
        'Cape Verdean Escudo': 'CVE',
        'Czech Koruna': 'CZK',
        'Djiboutian Franc': 'DJF',
        'Danish Krone': 'DKK',
        'Dominican Peso': 'DOP',
        'Algerian Dinar': 'DZD',
        'Egyptian Pound': 'EGP',
        'Eritrean Nakfa': 'ERN',
        'Ethiopian Birr': 'ETB',
        'Euro': 'EUR',
        'Fijian Dollar': 'FJD',
        'Falkland Islands Pound': 'FKP',
        'Faroese Króna': 'FOK',
        'British Pound Sterling': 'GBP',
        'Georgian Lari': 'GEL',
        'Guernsey Pound': 'GGP',
        'Ghanaian Cedi': 'GHS',
        'Gibraltar Pound': 'GIP',
        'Gambian Dalasi': 'GMD',
        'Guinean Franc': 'GNF',
        'Guatemalan Quetzal': 'GTQ',
        'Guyanaese Dollar': 'GYD',
        'Hong Kong Dollar': 'HKD',
        'Honduran Lempira': 'HNL',
        'Croatian Kuna': 'HRK',
        'Haitian Gourde': 'HTG',
        'Hungarian Forint': 'HUF',
        'Indonesian Rupiah': 'IDR',
        'Israeli New Shekel': 'ILS',
        'Manx Pound': 'IMP',
        'Indian Rupee': 'INR',
        'Iraqi Dinar': 'IQD',
        'Iranian Rial': 'IRR',
        'Icelandic Króna': 'ISK',
        'Jamaican Dollar': 'JMD',
        'Jordanian Dinar': 'JOD',
        'Japanese Yen': 'JPY',
        'Kenyan Shilling': 'KES',
        'Kyrgystani Som': 'KGS',
        'Cambodian Riel': 'KHR',
        'Kiribati Dollar': 'KID',
        'Comorian Franc': 'KMF',
        'South Korean Won': 'KPW',
        'Kuwaiti Dinar': 'KWD',
        'Cayman Islands Dollar': 'KYD',
        'Kazakhstani Tenge': 'KZT',
        'Laotian Kip': 'LAK',
        'Lebanese Pound': 'LBP',
        'Sri Lankan Rupee': 'LKR',
        'Liberian Dollar': 'LRD',
        'Lesotho Loti': 'LSL',
        'Libyan Dinar': 'LYD',
        'Moroccan Dirham': 'MAD',
        'Moldovan Leu': 'MDL',
        'Malagasy Ariary': 'MGA',
        'Macedonian Denar': 'MKD',
        'Myanmar Kyat': 'MMK',
        'Mongolian Tugrik': 'MNT',
        'Macanese Pataca': 'MOP',
        'Mauritanian Ouguiya': 'MRU',
        'Mauritian Rupee': 'MUR',
        'Maldivian Rufiyaa': 'MVR',
        'Malawian Kwacha': 'MWK',
        'Mexican Peso': 'MXN',
        'Malaysian Ringgit': 'MYR',
        'Mozambican Metical': 'MZN',
        'Namibian Dollar': 'NAD',
        'Nigerian Naira': 'NGN',
        'Nicaraguan Córdoba': 'NIO',
        'Norwegian Krone': 'NOK',
        'Nepalese Rupee': 'NPR',
        'New Zealand Dollar': 'NZD',
        'Omani Rial': 'OMR',
        'Panamanian Balboa': 'PAB',
        'Peruvian Nuevo Sol': 'PEN',
        'Papua New Guinean Kina': 'PGK',
        'Philippine Peso': 'PHP',
        'Pakistani Rupee': 'PKR',
        'Polish Zloty': 'PLN',
        'Paraguayan Guarani': 'PYG',
        'Qatari Rial': 'QAR',
        'Romanian Leu': 'RON',
        'Serbian Dinar': 'RSD',
        'Russian Ruble': 'RUB',
        'Rwandan Franc': 'RWF',
        'Saudi Riyal': 'SAR',
        'Solomon Islands Dollar': 'SBD',
        'Seychellois Rupee': 'SCR',
        'Sudanese Pound': 'SDG',
        'Swedish Krona': 'SEK',
        'Singapore Dollar': 'SGD',
        'Saint Helena Pound': 'SHP',
        'Sierra Leonean Leone': 'SLL',
        'Somali Shilling': 'SOS',
        'Surinamese Dollar': 'SRD',
        'South Sudanese Pound': 'SSP',
        'São Tomé and Príncipe Dobra': 'STN',
        'Syrian Pound': 'SYP',
        'Swazi Lilangeni': 'SZL',
        'Thai Baht': 'THB',
        'Tajikistani Somoni': 'TJS',
        'Turkmenistani Manat': 'TMT',
        'Tunisian Dinar': 'TND',
        'Tongan Paʻanga': 'TOP',
        'Turkish Lira': 'TRY',
        'Trinidad and Tobago Dollar': 'TTD',
        'Tuvaluan Dollar': 'TVD',
        'New Taiwan Dollar': 'TWD',
        'Tanzanian Shilling': 'TZS',
        'Ukrainian Hryvnia': 'UAH',
        'Ugandan Shilling': 'UGX',
        'United States Dollar': 'USD',
        'Uruguayan Peso': 'UYU',
        'Uzbekistan Som': 'UZS',
        'Venezuelan Bolívar': 'VES',
        'Vietnamese Dong': 'VND',
        'Vanuatu Vatu': 'VUV',
        'Samoan Tala': 'WST',
        'Central African Franc': 'XAF',
        'East Caribbean Dollar': 'XCD',
        'West African Franc': 'XOF',
        'CFP Franc': 'XPF',
        'Yemeni Rial': 'YER',
        'South African Rand': 'ZAR',
        'Zambian Kwacha': 'ZMW',
    }

    actual_dict = Currency.reverse_currency_dict()

    assert actual_dict == expected_dict
