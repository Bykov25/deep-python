#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class MaxHeap:

    def __init__(self) -> None:
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        pos = len(self.heap) - 1
        par = (pos - 1) // 2
        while pos > 0 and self.heap[pos] > self.heap[par]:
            self.heap[pos], self.heap[par] = self.heap[par], self.heap[pos]
            pos = par
            par = (pos - 1) // 2

    def pop(self) -> int:
        size = len(self.heap)
        max_val = self.heap[0]
        self.heap[0], self.heap[size - 1] = self.heap[size - 1], self.heap[0]
        del self.heap[size - 1]
        self.heapify(self.heap[0])
        return max_val

    def heapify(self, iterable: List[int]) -> None:
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            larg = i
            if left < len(self.heap) and self.heap[left] > self.heap[larg]:
                larg = left
            if right < len(self.heap) and self.heap[right] > self.heap[larg]:
                larg = right
            if larg == i:
                break
            self.heap[i], self.heap[larg] = self.heap[larg], self.heap[i]
            i = larg
