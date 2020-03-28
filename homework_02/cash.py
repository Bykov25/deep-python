#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cash:

    def __init__(self, count, *currency):
        self.count = count
        self.currency = currency

    def __add__(self, other):
        if other.currency:
            result = self.count + self.__operation(other)
        else:
            result = self.count + other.count
        return round(result, 2)

    def __operation(self, other):
        to_rubles = {'RUB': 1, 'USD': 81.13, 'AUD': 46.29,
                     'EUR': 87.75, 'CHF': 83.30, 'GBP': 93.69}
        if self.currency == other.currency:
            return other.count
        elif self.currency[0] == 'RUB':
            return other.count * to_rubles[other.currency[0]]
        else:
            rubles = other.count * to_rubles[other.currency[0]]
            return rubles * 1 / to_rubles[self.currency[0]]

    def __str__(self):
        return f"{self.count} {self.currency[0]}"

    def __repr__(self):
        return f"Cash({self.count}, '{self.currency[0]}')"
