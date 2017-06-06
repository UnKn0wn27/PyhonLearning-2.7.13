import unittest
from u_m import multiply

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3,4), 12)

    def test_numbers_a_4(self):
        self.assertEqual(multiply('a', 3), 'aaa')

if __name__ == '__main__':
    unittest.main()
