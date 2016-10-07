import unittest
from example.simple import soma


class SomaTest(unittest.TestCase):

    def test_soma_certa(self):
        result = soma(2, 2)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
