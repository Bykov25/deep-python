#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Matrix import Matrix
import matrix
import time
import random


def main():
    lst1 = [[random.randint(0, 4) for i in range(5)] for j in range(4)]
    lst2 = [[random.randint(0, 4) for i in range(3)] for j in range(5)]
    m1 = Matrix(lst1)
    m2 = Matrix(lst2)
    start = time.time()
    result_python = m1 * m2
    end = time.time()
    print(f"Python result:\n{result_python}\nTime: {end - start}")
    start = time.time()
    result_c = matrix.matrixmul(lst1, lst2)
    end = time.time()
    print(f"Python/C API result:\n{result_c}\nTime: {end - start}")

if __name__ == "__main__":
    main()
