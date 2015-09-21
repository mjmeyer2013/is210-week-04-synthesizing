#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Multiple complex functions"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """ This function will convert fahrenheit to celsius.

    Args:
        degrees(mix): what is being converted

    Returns:
        (dec) Converted Temperature

    Example:
        >>> fahrenheit_to_celsius(32)
        Decimal('0')
    """

    return (decimal.Decimal(degrees)-32)*5/9


def celsius_to_kelvin(degrees):
    """This function will conver celcius to kelvin.

    Args:
        degrees(dec): temputure wanting to be converted.

    Returns:
        decimal: New temputure in Kelvin

    Example:
        >>> celsius_to_kelvin(0)
        Decimal('273.15')
    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function will conver celcius to kelvin.

    Args:
        degrees(dec): temputure being converted

    Returns:
        decimal:Temputure in Kelvin

    Example:
        >>> fahrenheit_to_kelvin(32)
        Decimal(273.15)
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
