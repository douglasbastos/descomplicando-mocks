import unittest
from freezegun import freeze_time

from descomplicando.cenario_f_saudar_usuario import saudacao


class SaudacaoTest(unittest.TestCase):

    @freeze_time("2016-01-01 00:00:00")
    def test_deve_retornar_bom_dia(self):
        self.assertEqual(saudacao(), 'Bom dia')

    @freeze_time("2016-01-01 12:00:00")
    def test_deve_retornar_boa_tarde(self):
        self.assertEqual(saudacao(), 'Boa tarde')

    @freeze_time("2016-01-01 18:00:00")
    def test_deve_retornar_boa_noite(self):
        self.assertEqual(saudacao(), 'Boa noite')

if __name__ == '__main__':
    unittest.main()
