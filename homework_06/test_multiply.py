#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiply import multiply
from unittest.mock import patch
import unittest


class MultiplyTest(unittest.TestCase):

    def test_from_lesson(self):
        self.assertListEqual(multiply([1, 2, 3, 4]), [24, 12, 8, 6])
    
    def test_zero(self):
        self.assertListEqual(multiply([2, 0, 8]), [0, 16, 0])
    
    def test_two_numbers(self):
        self.assertListEqual(multiply([4, 5]), [5, 4])
    
    def test_negative_numbers(self):
        self.assertListEqual(multiply([-1, 5, 5, -3, 2, 8]), [-1200, 240, 240, -400, 600, 150])
        
    def test_simple(self):
        self.assertListEqual(multiply([-2, 5, -3, 1, 4, 0]), [0, 0, 0, 0, 0, 120])
    
    def test_instance(self):
        self.assertIsInstance(multiply([8, 1, 4, 5, 9]), list)
    
    def test_not_equal(self):
        self.assertNotEqual(multiply([10, 18]), [10, 18])

    def test_one_element_in_list(self):
        self.assertRaises(ValueError, multiply, [-1])
        
    def test_empty_list(self):
        self.assertRaises(ValueError, multiply, [])
    
    def test_contains_not_number(self):
        self.assertRaises(TypeError, multiply, [1, 'a', 3])
        
    def test_list_of_lists(self):
        self.assertRaises(TypeError, multiply, [[11], [1], [1, 2, 3]])
    
    def test_param_not_list(self):
        self.assertRaises(TypeError, multiply, "123")
    
    @patch('multiply.multiply', side_effect=lambda x: x[0])
    def test_side_effect(self, multiply):
        self.assertEqual(multiply([x for x in range(10**7)]), 0)
    
    @patch('multiply.multiply', return_value=10)
    def test_return_value(self, multiply):
        self.assertEqual(multiply([x for x in range(10**5)]), 10)


if __name__ == "__main__":
    unittest.main()
