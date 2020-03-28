#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyList(list):

    def __sub__(self, other):
        if len(self) == len(other):
            return [i - j for i, j in zip(self, other)]
        elif len(self) > len(other):
            return self.__operation(other, '-')
        else:
            result = other.__operation(self, '-')
            return [-1 * elem for elem in result]

    def __operation(self, other, sign):
        result = []
        for i in range(len(other)):
            if sign == '-':
                result.append(self[i] - other[i])
            else:
                result.append(self[i] + other[i])
        dif = len(self) - len(other)
        for j in range(dif):
            other.append(0)
            if sign == '-':
                result.append(self[i + j + 1] - other[i + j + 1])
            else:
                result.append(self[i + j + 1] + other[i + j + 1])
        for k in range(dif):
            del other[i + dif - k]
        return result

    def __add__(self, other):
        if len(self) == len(other):
            return [i + j for i, j in zip(self, other)]
        elif len(self) > len(other):
            return self.__operation(other, '+')
        else:
            return other.__operation(self, '+')

    def __eq__(self, other):
        return True if sum(self) == sum(other) else False

    def __ne__(self, other):
        return True if sum(self) != sum(other) else False

    def __lt__(self, other):
        return True if sum(self) < sum(other) else False

    def __gt__(self, other):
        return True if sum(self) > sum(other) else False

    def __le__(self, other):
        return True if sum(self) <= sum(other) else False

    def __ge__(self, other):
        return True if sum(self) >= sum(other) else False
