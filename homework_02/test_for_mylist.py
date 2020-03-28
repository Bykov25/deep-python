#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from mylist import MyList


def test_sub_1():
    list_1 = MyList([1, 2, 3, 4, 5])
    list_2 = MyList([1, 1, 1, 1, 1])
    assert list_1 - list_2 == [0, 1, 2, 3, 4]


def test_sub_2():
    list_1 = MyList([1, 2, 3, 4, 5])
    list_2 = MyList([3, 1])
    assert list_2 - list_1 == [2, -1, -3, -4, -5]


def test_add_1():
    list_1 = MyList([4, 1, 5, 8])
    list_2 = MyList([1, 1])
    assert list_2 + list_1 == [5, 2, 5, 8]


def tesst_add_2():
    list_1 = MyList([0, -1, -2])
    list_2 = MyList([90, 78, 100, 54])
    assert list_1 + list_2 == [90, 77, 98, 54]


def test_eq():
    list_1 = MyList([10, 3])
    list_2 = MyList([1, 4, 6, 2])
    assert list_1.__eq__(list_2) is True


def test_ne():
    list_1 = MyList([10, 3, 5])
    list_2 = MyList([1, 4, 6, 2])
    assert list_1.__ne__(list_2) is True


def test_lt():
    list_1 = MyList([0, 10])
    list_2 = MyList([1])
    assert list_1.__lt__(list_2) is False


def test_gt():
    list_1 = MyList([0, 1, 45])
    list_2 = MyList([100])
    assert list_1.__gt__(list_2) is False


def test_le():
    list_1 = MyList([0, 1, 2])
    list_2 = MyList([3])
    assert list_1.__le__(list_2) is True


def test_ge():
    list_1 = MyList([0, 1, 2, 10])
    list_2 = MyList([3, 4, 3])
    assert list_1.__ge__(list_2) is True
