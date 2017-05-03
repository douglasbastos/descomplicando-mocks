import unittest
from unittest import mock

from descomplicando import cenario_e_excecao

from descomplicando.cenario_e_excecao import mostrar_data_da_proxima_pybr, \
    SemPermissao


class ExibirDataPyBRTest(unittest.TestCase):

    def test_nao_deve_mostrar_evento_se_usuario_nao_tiver_permissao(self):
        with mock.patch.object(cenario_e_excecao,
                               'tem_permissao',
                               side_effect=SemPermissao):
            result = mostrar_data_da_proxima_pybr()
            self.assertEqual(result, 'Seu usuário não tem permissão')

    def test_deve_mostrar_evento_se_usuario_tiver_permissao(self):
        with mock.patch.object(cenario_e_excecao,
                               'tem_permissao',
                               return_value=True):
            result = mostrar_data_da_proxima_pybr()
            self.assertEqual(result, 'De 06 a 11 de Outubro')

if __name__ == '__main__':
    unittest.main()
