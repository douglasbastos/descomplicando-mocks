import unittest
from unittest import mock

from descomplicando.cenario_d_objeto_mockado_retornando_valor import \
    is_positive, redis


class IsNumberPositiveTest(unittest.TestCase):

    def test_deve_retornar_true_quando_numero_positivo(self):
        with mock.patch.object(redis, 'get', return_value=4):
            result = is_positive('key')
            self.assertTrue(result)

    def test_deve_retornar_false_quando_numero_nao_for_positivo(self):
        with mock.patch.object(redis, 'get', return_value=-4):
            result = is_positive('key')
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
