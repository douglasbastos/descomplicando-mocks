import unittest

from descomplicando.cenario_a_somar import somar


class SomarTest(unittest.TestCase):

    def test_deve_retornar_quatro_quando_dois_mais_dois(self):
        result = somar(2, 2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
