import unittest
from vector import Vector

class TestVectors(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        s = self.v1 + self.v2
        self.assertEqual(True, s == Vector(4.0, 4.0, 7.0))

    def test_mul(self):
        ans = 3 * self.v2
        self.assertEqual(True, ans == Vector(9.0, 18.0, 27.0))

    def test_div(self):
        ans = 3 / self.v2
        self.assertEqual(True, ans == Vector(1.0, 2.0, 3.0))

    #def test_normalize(self):
