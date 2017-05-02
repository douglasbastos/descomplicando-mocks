import os
import unittest
from unittest import mock

from descomplicando.cenario_b_remove_lista_de_arquivos import remove_files


class RemoveFilesTest(unittest.TestCase):

    def test_deve_remover_arquivos(self):
        lista_arquivos = ['abc.txt', 'xyz.txt', 'def.txt']
        with mock.patch.object(os, 'remove') as qualquercoisa:
            remove_files(lista_arquivos)
            self.assertEqual(3, qualquercoisa.call_count)


if __name__ == '__main__':
    unittest.main()
