#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from cash import Cash


def test_1():
    a = Cash(45, 'RUB')
    b = Cash(31, 'USD')
    assert a + b == 2560.03


def test_2():
    a = Cash(1, 'AUD')
    b = Cash(5, 'GBP')
    assert a + b == 11.12


def test_3():
    a = Cash(38, 'CHF')
    b = Cash(27, 'EUR')
    assert a + b == 66.44


def test_4():
    a = Cash(5)
    b = Cash(10, 'USD')
    assert a + b == 15
    assert b + a == 15


def test_str():
    a = Cash(5, 'USD')
    assert a.__str__() == '5 USD'


def test_repr():
    a = Cash(18, 'EUR')
    assert a.__repr__() == "Cash(18, 'EUR')"