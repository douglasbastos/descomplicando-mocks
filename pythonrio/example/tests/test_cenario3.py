from unittest import TestCase, mock
from example.cenario3 import info_evento, NotPermission


class VerEventosTest(TestCase):

    def test_deve_mostrar_evento_se_usuario_tiver_permissao(self):
        with mock.patch('example.cenario3.tem_permissao', return_value=True):
            self.assertEqual(info_evento('pythonrio'),
                             'Rio de Janeiro')

    def test_nao_deve_mostrar_evento_se_usuario_nao_tiver_permissao(self):
        with mock.patch('example.cenario3.tem_permissao', side_effect=NotPermission):
            self.assertEqual(info_evento('pythonrio'),
                             'Você não tem permissão para essa operação')

    def test_deve_mostrar_nenhum_evento_encontrado_quando_chave_incorreta(self):
        with mock.patch('example.cenario3.tem_permissao', return_value=True):
            result = info_evento('java')
            self.assertEqual(result, 'Nenhum evento encontrado')
