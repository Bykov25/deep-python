#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from MedianFinder import MedianFinder


def test_1():
    m = MedianFinder()
    m.addNum(1)
    m.addNum(0)
    m.addNum(5)
    m.addNum(2)
    assert m.findMedian() == 1.5


def test_2():
    m = MedianFinder()
    m.addNum(-1)
    m.addNum(2)
    m.addNum(2)
    m.addNum(14)
    m.addNum(0)
    assert m.findMedian() == 2.0


def test_3():
    m = MedianFinder()
    assert m.findMedian() == "Empty list"


def test_4():
    m = MedianFinder()
    m.addNum(-1)
    assert m.findMedian() == -1.0


def test_5():
    m = MedianFinder()
    m.addNum(1)
    m.addNum(0)
    m.addNum(5)
    m.addNum(3)
    m.addNum(8)
    assert m.lst == [0, 1, 3, 5, 8]
    assert m.findMedian() == 3.0
