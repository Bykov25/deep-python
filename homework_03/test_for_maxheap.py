#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from MaxHeap import MaxHeap


def test_1():
    h = MaxHeap()
    h.push(2)
    h.push(1)
    h.push(5)
    h.push(26)
    assert h.pop() == 26
    assert h.pop() == 5
    assert h.pop() == 2
    assert h.pop() == 1
    assert h.pop() == "Empty heap"


def test_2():
    h = MaxHeap()
    h.push(-10)
    h.push(3)
    h.push(7)
    h.push(21)
    h.push(-5)
    assert h.heap == [21, 7, 3, -10, -5]


def test_3():
    h = MaxHeap()
    assert h.pop() == "Empty heap"


def test_4():
    h = MaxHeap()
    h.push(-1)
    h.push(0)
    h.push(0)
    h.push(0)
    h.push(2)
    h.push(2)
    assert h.pop() == 2
    assert h.pop() == 2
    assert h.pop() == 0
    assert h.pop() == 0
    assert h.pop() == 0
    assert h.pop() == -1
    assert h.pop() == "Empty heap"
