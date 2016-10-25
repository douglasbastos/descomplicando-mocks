import os
from unittest import TestCase, mock
from example.cenario4 import remove_files


class RemoveFilesTest(TestCase):

    def test_deve_remover_arquivos(self):
        lista_arquivos = ['abc.txt', 'xyz.txt', 'def.txt']
        with mock.patch.object(os, 'remove') as remove:
            remove_files(lista_arquivos)
            # Quantas vezes remove foi chamada
            self.assertEqual(3, remove.call_count)
            # Verifica argumentos passada a cada chamada
            self.assertEqual([mock.call('abc.txt'), mock.call('xyz.txt'), mock.call('def.txt')],
                             remove.call_args_list)
