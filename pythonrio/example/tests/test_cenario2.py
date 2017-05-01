from unittest import TestCase, mock
from example.cenario2 import is_positive


class IsNumberPositiveTest(TestCase):

    def test_deve_retornar_true_quando_numero_positivo(self):
        with mock.patch('example.cenario2.get_value', return_value=4):
            result = is_positive('key')
            self.assertTrue(result)

    def test_deve_retornar_false_quando_numero_nao_for_positivo(self):
        with mock.patch('example.cenario2.get_value', return_value=-4):
            result = is_positive('key')
            self.assertFalse(result)
