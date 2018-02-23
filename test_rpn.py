import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_substract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
    def test_multiply(self):
        result = rpn.calculate('2 3 *')
        self.assertEqual(6, result)
    def test_multiplies(self):
        result = rpn.calculate('2 3 * 4 *')
        self.assertEqual(24, result)
