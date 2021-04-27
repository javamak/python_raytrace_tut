import unittest
from color import Color

class TestColors(unittest.TestCase):
    def setUp(self):
        self.c1 = Color(1, 2, 3)
        self.c2 = Color(1, 2, 3)

    def test_add(self):
        assert (self.c1 + self.c2, Color(2, 4, 6))

if __name__ == '__main__':
    unittest.main()
