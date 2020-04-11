#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from LRUcache import LRUCache


def test_1():
    cache = LRUCache(100)
    cache.set_item('Jesse', 'Pinkman')
    cache.set_item('Walter', 'White')
    cache.set_item('Jesse', 'James')
    assert cache.get_item('Jesse') == 'James'
    cache.del_item('Walter')
    assert cache.get_item('Walter') == ''


def test_2():
    cache = LRUCache(3)
    cache.set_item('a', 1)
    cache.set_item('b', 2)
    cache.set_item('c', 3)
    cache.del_item('a')
    assert cache.get_item('a') == ''
    cache.get_item('b')
    assert cache.cache_values == {'c': 3, 'b': 2}


def test_3():
    cache = LRUCache(1)
    cache.set_item('a', 1)
    cache.set_item('b', 2)
    assert cache.get_item('a') == ''
    assert cache.get_item('b') == 2
    assert cache.cache_values == {'b': 2}
