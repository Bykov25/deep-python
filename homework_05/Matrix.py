#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


class Matrix:
    
    def __init__(self, matrix_representation):
        self.matrix_representation = matrix_representation
        self.shape = []
        self.d = self.__dimension(matrix_representation)
        if self.d is not None:
            self.items = matrix_representation
            for i in range(self.d - 1):
                self.items = [el for el in itertools.chain.from_iterable(self.items)]
            if Matrix.__count_of_items(self.shape) != len(self.items):
                raise ValueError
        else:
            raise ValueError
    
    def __dimension(self, test, d=0):
        if not isinstance(test, list):
            return None if d == 0 else d
        else:
            d += 1
            self.shape.append(len(test))
            d = self.__dimension(test[0], d)
            return d
    
    @staticmethod
    def __count_of_items(shape):
        result = 1
        for i in shape:
            result *= i
        return result
    
    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError
        new_items = [i + j for i, j in zip(self.items, other.items)]
        cols = self.shape[1]
        strings = self.shape[0]
        representation = [new_items[i * cols:i * cols + cols] for i in range(strings)]
        return Matrix(representation)
    
    def __str__(self):
        result = ''
        for lst in self.matrix_representation:
            string = ''
            for char in lst:
                string += str(char) + ' '
            result += string.strip() + '\n'
        return result.strip()
    
    def __repr__(self):
        return f"Matrix({self.matrix_representation})"
    
    def __mul__(self, other):
        if isinstance(other, int):
            new_items = [other * i for i in self.items]
            cols = self.shape[1]
            strings = self.shape[0]
            representation = [new_items[i * cols:i * cols + cols] for i in range(strings)]
            return Matrix(representation)
        if isinstance(other, Matrix):
            return self.__matmul__(other)
        else:
            raise ValueError
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __getitem__(self, indexes):
        ptr = 0
        if self.d == 1:
            return self.items[indexes]
        for i in range(len(indexes)):
            if indexes[i] >= self.shape[i]:
                raise IndexError
            ptr += int(Matrix.__count_of_items(self.shape[i + 1:])) * indexes[i]
        return self.items[ptr]
    
    def __truediv__(self, other):
        if isinstance(other, int):
            new_items = [i / other for i in self.items]
            cols = self.shape[1]
            strings = self.shape[0]
            representation = [new_items[i * cols:i * cols + cols] for i in range(strings)]
            return Matrix(representation)
        else:
            raise ValueError
    
    def transpose(self):
        zip_m = list(zip(*self.matrix_representation))
        representation = []
        for row in zip_m:
            representation.append(list(row))
        return Matrix(representation)
    
    def __contains__(self, item):
        return True if item in self.items else False
    
    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError
        other_tr = list(zip(*other.matrix_representation))
        representation = [[sum(i * j for i, j in zip(row_self, col_other)) for col_other in other_tr] for row_self in self.matrix_representation]
        return Matrix(representation)
<<<<<<< HEAD
    
    def __eq__(self, other):
        if self.matrix_representation == other.matrix_representation:
            return True
        return False
=======
        
 
>>>>>>> parent of b57fe54... add extension
