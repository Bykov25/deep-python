#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache_values = OrderedDict()

    def get_item(self, key: str) -> str:
        if key not in self.cache_values:
            return ''
        self.cache_values.move_to_end(key, last=True)
        return self.cache_values[key]

    def set_item(self, key: str, value: str) -> None:
        if len(self.cache_values) == self.capacity:
            self.del_item(next(iter(self.cache_values)))
        self.cache_values[key] = value

    def del_item(self, key: str) -> None:
        del self.cache_values[key]
