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
    def test_divide(self):
        result = rpn.calculate('6 2 /')
        self.assertEqual(3, result)
    def test_divides(self):
        result = rpn.calculate('6 2 / 3 /')
        self.assertEqual(1, result)
    def test_bitwiseand(self):
        result = rpn.calculate('10 3 &')
        self.assertEqual(2 ,result)
    def test_bitwiseor(self):
        result = rpn.calculate('10 3 |')
        self.assertEqual(11, result)
    def test_bitwisenot(self):
        result = rpn.calculate('10 ~')
        self.assertEqual(-11, result)
    def test_rotate(self):
        result = rpn.calculate('1 2 3 r')
        self.assertEqual([3, 2, 1], result)
    def test_summation(self):
        result = rpn.calculate('1 2 3 4 5 6 7 8 9 10 s')
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55], result)
    def test_exponentiationPos(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
    def test_exponentiationZ(self):
        result = rpn.calculate('2 0 ^')
        self.assertEqual(1, result)
    def test_exponentiationNeg(self):
        result = rpn.calculate('2 -1 ^')
        self.assertEqual(0.5, result)
