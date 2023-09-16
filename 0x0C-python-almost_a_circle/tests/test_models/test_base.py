#!/usr/bin/python3
"""Test class for the Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_init_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_2(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_init_with_id(self):
        b2 = Base(9)
        self.assertEqual(9, b2.id)

    def 

if __name__ == "__main__":
    unittest.main()
