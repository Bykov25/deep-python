#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Matrix import Matrix
import unittest


class MatrixTest(unittest.TestCase):
    
    def test_add(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        m2 = Matrix([[-1, 3], [8, 6], [9, 0]])
        result = Matrix([[0, 5], [11, 10], [14, 6]])
        self.assertEqual(m1 + m2, result)
    
    def test_mul(self):
        m1 = Matrix([[1, 6], [4, 8]])
        result = Matrix([[-1, -6], [-4, -8]])
        self.assertEqual(m1 * -1, result)
    
    def test_truediv(self):
        m1 = Matrix([[2, 4], [6, 8]])
        result = Matrix([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(m1 / 2, result)
    
    def test_matmul(self):
        m1 = Matrix([[0, -4], [5, 2], [4, -9]])
        m2 = Matrix([[2, 4], [6, 8]])
        result = Matrix([[-24, -32], [22, 36], [-46, -56]])
        self.assertEqual(m1 * m2, result)
    
    def test_transpose(self):
        m1 = Matrix([[0, 2], [-5, 1], [3, -7]])
        result = Matrix([[0, -5, 3], [2, 1, -7]])
        self.assertEqual(m1.transpose(), result)
    
    def test_str(self):
        m1 = Matrix([[2, 4], [6, 8]])
        self.assertEqual(m1.__str__(), "2 4\n6 8")
    
    def test_repr(self):
        m1 = Matrix([[1, 0], [5, 4]])
        self.assertEqual(m1.__repr__(), "Matrix([[1, 0], [5, 4]])")
    
    def test_contains(self):
        m1 = Matrix([[6, 0], [-1, 8]])
        self.assertIn(6, m1)
    
    def test_getitem(self):
        m1 = Matrix([[6, 5], [-1, 3]])
        self.assertEqual(m1[(0, 1)], 5)
    
    def test_error_dimension(self):
        self.assertRaises(ValueError, Matrix, [[6, 5], [-1, 3], [0, 1, 0]])
    
    def test_error_representation(self):
        self.assertRaises(ValueError, Matrix, ([1,4], [1, 1]))
    
    def test_error_add(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        m2 = Matrix([[-1, 3], [8, 6], [9, 0], [1, 1]])
        self.assertRaises(ValueError, m1.__add__, m2)
    
    def test_error_mul(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        self.assertRaises(ValueError, m1.__mul__, 3.2)
    
    def test_error_truediv(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        self.assertRaises(ValueError, m1.__truediv__, 1.5)
    
    def test_error_getitem(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        self.assertRaises(IndexError, m1.__getitem__, (0, 2))
    
    def test_error_matmul(self):
        m1 = Matrix([[0, -4], [5, 2], [4, -9]])
        m2 = Matrix([[2, 4], [6, 8], [3, 4]])
        self.assertRaises(ValueError, m1.__matmul__, m2)

if __name__ == "__main__":
    unittest.main()
