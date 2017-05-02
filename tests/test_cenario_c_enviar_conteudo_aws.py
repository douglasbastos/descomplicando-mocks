import unittest
from unittest import mock

from descomplicando.cenario_c_enviar_conteudo_aws import enviar_conteudo_aws


class SendContentTest(unittest.TestCase):

    def test_enviar_conteudo_aws(self):
        with mock.patch('descomplicando.cenario_c_enviar_conteudo_aws.boto3') as mocked:
            enviar_conteudo_aws('helloword.txt', 'Hello Word')
            mocked.send.called

if __name__ == '__main__':
    unittest.main()
