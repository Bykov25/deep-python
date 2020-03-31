#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def __binary_index_search(self, num: int) -> int:
        left = -1
        right = len(self.lst)
        if right == 0:
            return 0
        if self.lst[0] >= num:
            return 0
        while right > left + 1:
            middle = (right + left) // 2
            if self.lst[middle] >= num:
                right = middle
            else:
                left = middle
        return right

    def addNum(self, num: int) -> None:
        index = self.__binary_index_search(num)
        self.lst.insert(index, num)

    def findMedian(self) -> float:
        size = len(self.lst)
        if size % 2 == 0:
            left = size // 2 - 1
            right = size // 2
            return (self.lst[left] + self.lst[right]) / 2
        else:
            return sum(self.lst) / size
